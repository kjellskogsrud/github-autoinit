import requests # pip install requests to make this work
import os
import sys

# CHANGE THIS
import loginDetails # This is where I keep you userName and token, just remove this line
userName = loginDetails.username # replace getUsername() with "yourusername"
token = loginDetails.token # replace getToken() with "yourtoken"
# to get a token go here, and make a personal access token: https://github.com/settings/tokens
# CHANGE THIS


defaultgitIgnoreFile = open(r'{path}'.format(path=sys.argv[0].replace("git-init.py","defaultGitIgnore")),'r')

calledPath = sys.argv[1]

# Check of this folder has a git repo
if os.path.exists(r'{path}\.git'.format(path=calledPath)) is not False:
    exit(0) # And exit if it does.

# Not a .git folder, then lets git init
os.system("git init {path}".format(path=calledPath))

# Is there a README.md file in that folder that we can open?
# If there is, we open it, and if not it is created.
readme = open(r'{path}\README.md'.format(path=calledPath), 'w+')
readme.close()

os.chdir(calledPath) # enter the folder of the repo now to do some git work
os.system("git commit -m empty --allow-empty") # make the first empty commit

# Make the .gitignore file based on the default file
gitIgnore = open(r'{path}\.gitignore'.format(path=calledPath),'w+')
gitIgnore.write(defaultgitIgnoreFile.read())
gitIgnore.close()
defaultgitIgnoreFile.close()

os.system("git add README.md") # add README.md
os.system("git add .gitignore") # add .gitignore

os.system("git commit -m \"initial commit\"")

# Now lets push everything to github
folderName = os.path.basename(os.path.normpath(calledPath)) # the folder name is the repo name

# Make a repo json
newRepo = {
  "name": folderName,
  "description": "Made with git-init.py",
  "homepage": "",
  "private": False,
  "has_issues": False,
  "has_projects": False,
  "has_wiki": False
}

# Make github make that repo
resp = requests.post('https://api.github.com/user/repos', auth=(userName,token), json=newRepo)
if resp.status_code != 200:
    # something went wrong ?
    print(resp.status_code)

# Get the details of the repo back from github
resp = requests.get('https://api.github.com/repos/{user}/{repo}'.format(user=userName,repo=folderName), auth=(userName,token))

# Get the ssh_url from that repo
sshURL = resp.json()['ssh_url']

# Add the remote
os.system("git remote add origin {remoteURL}".format(remoteURL=sshURL))

# Push to GitHub
os.system("git push origin master")

input("Press enter to exit")
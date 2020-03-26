import requests # pip install requests to make this work
import os
import sys

# CHANGE THIS
import loginDetails # This is where I keep the userName and token, just remove this line
userName = loginDetails.username # replace loginDetails.username with "yourusername"
token = loginDetails.token # replace loginDetails.token with "yourtoken"
# to get a token go here, and make a personal access token: https://github.com/settings/tokens
# CHANGE THIS

calledPath = sys.argv[1]

# Check of this folder has a git repo
if os.path.exists(r'{path}\.git'.format(path=calledPath)) is not False:
    exit(0) # And exit if it does.

# Not a .git folder, then lets git init
os.system("git init {path}".format(path=calledPath))

os.chdir(calledPath) # enter the folder of the repo now to do some git work
os.system("git commit -m empty --allow-empty") # make the first empty commit

# Is there a README.md file in that folder that we can open?
# If there is, we open it, and if not it is created.
readme = open(r'{path}\README.md'.format(path=calledPath), 'a+')
readme.close()

# Make the .gitignore file based on the default file
defaultgitIgnoreFile = open(r'{path}'.format(path=sys.argv[0].replace("git-init.py","defaultGitIgnore")),'r') # open the default file
gitIgnore = open(r'{path}\.gitignore'.format(path=calledPath),'a+') # open the .gitignore files
gitIgnore.write(defaultgitIgnoreFile.read()) # write the .gitignore file with the contents of the default file. 

# close both files
gitIgnore.close() 
defaultgitIgnoreFile.close()

os.system("git add README.md") # add README.md
os.system("git add .gitignore") # add .gitignore

os.system("git commit -m \"initial commit\"") # commit both files as the inital commit

# Moving on to github
folderName = os.path.basename(os.path.normpath(calledPath)) # get the the folder name to use for the repo name

# Make a repo json
# You can change this to what your defaults are.
newRepo = {
  "name": folderName,
  "description": "Made with git-init.py",
  "homepage": "",
  "private": False,
  "has_issues": False,
  "has_projects": False,
  "has_wiki": False
}

# Tell github to make that repo
resp = requests.post('https://api.github.com/user/repos', auth=(userName,token), json=newRepo)
if resp.status_code != 201: # we expect 201 here. That means "Created"
    # something went wrong ?
    print(resp.status_code) 

# The respons from the post request would be the repo details so we get sshURL from that.
sshURL = resp.json()['ssh_url']

# Add the remote ssh URL as origin
os.system("git remote add origin {remoteURL}".format(remoteURL=sshURL))

# Push to GitHub
os.system("git push origin master")

# Stop the script here and wait for the user to click exit.
# This is optional, if you don't like that just comment the line away. 
# I like to keep it up to see that i did't get any errors along the way. 
input("Press enter to exit")
# github-autoinit
This is a small python script that automates a few key steps when I make new git repositories. 

## What does it do?
It is made to be used on windows as a right-click option on folders. So simply right-click a folder, select "Auto init to GitHub" and BAHM! stuff happens.

### What stuff?
* If this folder is not a git repository, run git init on it. 
* Make an empty README.md file
* Make a .gitignore file based on the defaultGitIgnore file
* Commit no files with the message "empty" ([why empty commits?](https://gist.github.com/kjellskogsrud/d824c38f76e38010156d0bc80dbd3c62))
* Add .gitignore and README.md
* Commit those files with the message "inital commit" 
* Make a github repository with the same name as the folder
* Add that repository as the origin remote
* Push to master to origin 

### It doesn't work!
It does, but there are some things it assumes you have.
* It uses SSH for authentication with the remote, and for that to work in this way it assumes you have an SSH agent and have setup your github account with SSH keys.
* It want's a username and personal token from github to use the API. A personal token is not the same as your password. [You get tokens her](https://github.com/settings/tokens)

## Installation?
The file is made to be used as a windows right-click option on directories. A .reg files is included that can be used to add the option.
Remember to change the paths in the reg file to where your files are located. The two paths you need are the location of python.exe and the location of git-init.py(from this repo)
NB! Don't forget to escape the slashes in those paths. IE. "C:\\\Program files\\\Python38\\\python.exe" NOT "C:\Program files\Python38\python.exe"
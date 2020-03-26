# github-autoinit
This is a small python script that automates a few key steps when I make new git repositories. 

## What does it do?
It is made to be used on windows as a right-click option on folders. So simply right-click a folder, select "Auto init to GitHub" and BAHM! stuff happens.

What stuff?
* If this folder is not a git repository, run git init on it. 
* Make an empty README.md file
* Make a .gitignore file based on the defaultGitIgnore file
* Commit no files with the message "empty"
* Add .gitignore and README.md
* Commit those files with the message "inital commit" 
* Make a github repository with the same name as the folder
* Add that repository as the origin remote
* Push to master to origin 
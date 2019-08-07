# How to Clone a Git Repository from the Unix Command Line
Note: <> don't need to be typed. They mean that the thing being typed is a placeholder. If you see something like ```<esc>``` or ```<escape>```, it doesn't mean type ```"<escape>"```, it means push the escape key. Another example: ```git clone <url>``` means you type something *like* ```git clone https://github.com/inf108/thisWillLookDifferentEveryTime```.

1. Clone this repository locally using the url for this repository. This will create a new directory that copies the contents of this repository.

```git clone <url>```

2. Change directory to work inside your new repository directory instead of in the directory that contains it.

```cd <directory name>```

3. Create a branch

```git checkout -b <yourName>```

4. Change anything. You can edit a file that is already there or start a new file. It's very common for people to just create an empty file straight from the command line, but any edit will do. To create an empty file, use the ```touch``` command

```
touch <filename>
```

5. Commit the change. Your message should describe what you just did in a way that would be useful to someone who only knows what you did by reading your messages. Think about what you see when you get a software update. If it says that it is a security update, you take it urgently and install the upgrade right away. If it adds a feature you don't want, you might not upgrade. In a professional setting, this message tells the person responsible for merging everyone's work together what this update does and helps them prioritize their effort.

```
git add <filename>
git commit -m "<message>"
```

6. Link to remote repository and push. You need a different label for each repository. Setting up your repository this way creates a bookmark. You'll be able to just type ```git push``` to keep pushing to this branch. If you wanted to make a new branch, you would do step 3 again and redo ```git push -u <label> <newBranchName>```. 

```
git remote add <label> <url>
git push -u <label> <branchName>
```

7. Each time you make a meaningful, testable change to anything in the repository, repeat step 5. As a rule, you should try to commit more often than you think you do. 

8. Whenever you are at the end of a work session or complete something substantive, push (step 6). This creates a cloud backup.

9. Whenever you have completed something substantive (in a class setting, this means an assignment; in a work setting this usually means you've completed a component or finished fixing a bug) go to the url on github and click ```pull request``` and that creates an area where your instructor (or lead programmer/manager/whatever) can give you feed back on your code (or incorporate it into the master branch for the team to use in a professional setting). 

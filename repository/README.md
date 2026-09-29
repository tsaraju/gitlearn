Git Repository from Scratch

Create a Python project locally and initialize it using Git. Add at least 4 Python files. 
Demonstrate git init, git status, git add, git commit, git log, git diff, and .gitignore. 
Make at least 5 meaningful commits and publish the repository on GitHub.

Sample output:
Create a Python project locally and initialize it using Git. Add at least 4 Python files. 
Demonstrate git init, git status, git add, git commit, git log, git diff, and .gitignore. 
Make at least 5 meaningful commits and publish the repository on GitHub.

PS F:\Euron\GitHub\gitlearn\repository> git status   
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.py

no changes added to commit (use "git add" and/or "git commit -a")
PS F:\Euron\GitHub\gitlearn\repository> git add a.py              
PS F:\Euron\GitHub\gitlearn\repository> git commit -m "Update diff command info"
[master 768edb0] Update diff command info
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\repository> git status                              
On branch master
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\repository> git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b.py
        c.py

nothing added to commit but untracked files present (use "git add" to track)
PS F:\Euron\GitHub\gitlearn\repository> git add .                               
PS F:\Euron\GitHub\gitlearn\repository> git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   b.py
        new file:   c.py

PS F:\Euron\GitHub\gitlearn\repository> git commit -m "Promoting 2nd and 3rd files"
[master bbcc883] Promoting 2nd and 3rd files
 2 files changed, 2 insertions(+)
 create mode 100644 b.py
 create mode 100644 c.py
PS F:\Euron\GitHub\gitlearn\repository> git status                                 
On branch master
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\repository> git log --oneline
bbcc883 (HEAD -> master) Promoting 2nd and 3rd files
768edb0 Update diff command info
89690a2 First file
PS F:\Euron\GitHub\gitlearn\repository> git status       
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        d.py

nothing added to commit but untracked files present (use "git add" to track)
PS F:\Euron\GitHub\gitlearn\repository> git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)
PS F:\Euron\GitHub\gitlearn\repository> git add .gitignore  
PS F:\Euron\GitHub\gitlearn\repository> git status        
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore

PS F:\Euron\GitHub\gitlearn\repository> git commit -m "Adding git ignore file"     
[master 99b362f] Adding git ignore file
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore
PS F:\Euron\GitHub\gitlearn\repository> git status                            
On branch master
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\repository> git status
On branch master
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\repository> git status
On branch master
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\repository> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   c.py

no changes added to commit (use "git add" and/or "git commit -a")
PS F:\Euron\GitHub\gitlearn\repository> git add c.py                          
PS F:\Euron\GitHub\gitlearn\repository> git commit -m "Updating 3rd file"
[master 46c4c06] Updating 3rd file
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\repository> git status                            
On branch master
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\repository> git log --oneline
46c4c06 (HEAD -> master) Updating 3rd file
99b362f Adding git ignore file
bbcc883 Promoting 2nd and 3rd files
768edb0 Update diff command info
89690a2 First file
PS F:\Euron\GitHub\gitlearn\repository> 
 *  History restored 

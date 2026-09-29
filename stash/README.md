Git Stash Practical

Start implementing a feature but do not commit it. Use git stash to temporarily save the work. 
Switch to another branch and make an urgent fix. 
Return to the original branch and demonstrate git stash list, git stash show, git stash apply, git stash pop, and git stash drop. 
Explain the difference between apply and pop.

Sample Output:

PS F:\Euron\GitHub\gitlearn\stash> git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   profile.py

PS F:\Euron\GitHub\gitlearn\stash> git commit -m "Initial commit"
[main (root-commit) 69e35d6] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 profile.py
PS F:\Euron\GitHub\gitlearn\stash> git status                    
On branch main
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\stash> git checkout -b feature       
Switched to a new branch 'feature'
PS F:\Euron\GitHub\gitlearn\stash> git status             
On branch feature
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\stash> git status
On branch feature
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.py

nothing added to commit but untracked files present (use "git add" to track)
PS F:\Euron\GitHub\gitlearn\stash> git status
On branch feature     
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.py

nothing added to commit but untracked files present (use "git add" to track)
PS F:\Euron\GitHub\gitlearn\stash> git stash push -m "WIP: profile editing"^C
PS F:\Euron\GitHub\gitlearn\stash> git branch
* feature
  main
PS F:\Euron\GitHub\gitlearn\stash> git checkout -b feature^C     
PS F:\Euron\GitHub\gitlearn\stash> git stash push -m "WIP: profile editing"
No local changes to save
PS F:\Euron\GitHub\gitlearn\stash> git add test.py                         
PS F:\Euron\GitHub\gitlearn\stash> git stash push -m "WIP: profile editing"
Saved working directory and index state On feature: WIP: profile editing
PS F:\Euron\GitHub\gitlearn\stash> git stash
No local changes to save
PS F:\Euron\GitHub\gitlearn\stash> git stash list
stash@{0}: On feature: WIP: profile editing
PS F:\Euron\GitHub\gitlearn\stash> git status                              
On branch feature
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.py

nothing added to commit but untracked files present (use "git add" to track)

PS F:\Euron\GitHub\gitlearn\stash> git add test.py                           
PS F:\Euron\GitHub\gitlearn\stash> git stash push -m "WIP: profile editing 2"
Saved working directory and index state On feature: WIP: profile editing 2
PS F:\Euron\GitHub\gitlearn\stash> git stash list
stash@{0}: On feature: WIP: profile editing 2
stash@{1}: On feature: WIP: profile editing
PS F:\Euron\GitHub\gitlearn\stash> git branch
* feature
  main
PS F:\Euron\GitHub\gitlearn\stash> git checkout -b main
fatal: a branch named 'main' already exists
PS F:\Euron\GitHub\gitlearn\stash> git switch main
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\stash> git status                                
On branch main
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\stash> git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   profile.py

no changes added to commit (use "git add" and/or "git commit -a")
PS F:\Euron\GitHub\gitlearn\stash> git add .\profile.py
PS F:\Euron\GitHub\gitlearn\stash> git status          
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   profile.py

PS F:\Euron\GitHub\gitlearn\stash> git commit -m "urgent fix"
[main cbec7dc] urgent fix
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\stash> git status                
On branch main
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\stash> git branch
  feature
* main
PS F:\Euron\GitHub\gitlearn\stash> git switch feature
Switched to branch 'feature'
PS F:\Euron\GitHub\gitlearn\stash> git status        
On branch feature
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\stash> git stash list            
stash@{0}: On feature: WIP: profile editing 2
stash@{1}: On feature: WIP: profile editing
PS F:\Euron\GitHub\gitlearn\stash> git stash apply
On branch feature
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test.py

PS F:\Euron\GitHub\gitlearn\stash> git status     
On branch feature
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test.py

PS F:\Euron\GitHub\gitlearn\stash> git stash list 
stash@{0}: On feature: WIP: profile editing 2
stash@{1}: On feature: WIP: profile editing
PS F:\Euron\GitHub\gitlearn\stash> git stash pop  
On branch feature
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test.py

Dropped refs/stash@{0} (fb788090c8532c6faafdb2d21fccdf801361bc9b)
PS F:\Euron\GitHub\gitlearn\stash> git stash list
stash@{0}: On feature: WIP: profile editing
PS F:\Euron\GitHub\gitlearn\stash> git stash drop
Dropped refs/stash@{0} (a96a530308f3e25f1d5bd58f6bf35d6b0bf67ede)
PS F:\Euron\GitHub\gitlearn\stash> git stash list

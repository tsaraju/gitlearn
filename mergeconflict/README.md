Create and Resolve a Real Merge Conflict

Create two branches from the same base. Modify the same line of the same file differently in both branches. 
Merge the first branch into main, then attempt to merge the second branch so that Git produces a merge conflict. 
Resolve the conflict manually and commit the resolution.

Sample Output:

PS F:\Euron\GitHub\gitlearn\mergeconflict> git init -b main
Initialized empty Git repository in F:/Euron/GitHub/gitlearn/mergeconflict/.git/
PS F:\Euron\GitHub\gitlearn\mergeconflict> git checkout main
error: pathspec 'main' did not match any file(s) known to git
PS F:\Euron\GitHub\gitlearn\mergeconflict> git checkout -b main
Switched to a new branch 'main'
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        merge.py

nothing added to commit but untracked files present (use "git add" to track)
PS F:\Euron\GitHub\gitlearn\mergeconflict> git add .\merge.py  
PS F:\Euron\GitHub\gitlearn\mergeconflict> git commit -m "Initial commit"
[main (root-commit) b3c73e0] Initial commit
 1 file changed, 2 insertions(+)
 create mode 100644 merge.py
PS F:\Euron\GitHub\gitlearn\mergeconflict> git branch
* main
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status
On branch main
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\mergeconflict> git checkout -b dev1
Switched to a new branch 'dev1'
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status          
On branch dev1
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status
On branch dev1
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   merge.py

no changes added to commit (use "git add" and/or "git commit -a")
PS F:\Euron\GitHub\gitlearn\mergeconflict> git add .\merge.py            
PS F:\Euron\GitHub\gitlearn\mergeconflict> git commit -m "Developer 1 commit" 
[dev1 9ff7b27] Developer 1 commit
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status                        
On branch dev1
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\mergeconflict> git checkout main                 
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\mergeconflict> git branch
  dev1
* main
PS F:\Euron\GitHub\gitlearn\mergeconflict> git checkout -b dev2
Switched to a new branch 'dev2'
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status          
On branch dev2
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\mergeconflict> git add .\merge.py                
PS F:\Euron\GitHub\gitlearn\mergeconflict> git commit -m "Developer 2 commit"
[dev2 9602b47] Developer 2 commit
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\mergeconflict> git status                        
On branch dev2
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\mergeconflict> git branch
  dev1
* dev2
  main
PS F:\Euron\GitHub\gitlearn\mergeconflict> git switch main
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\mergeconflict> git branch     
  dev1
  dev2
* main
PS F:\Euron\GitHub\gitlearn\mergeconflict> git merge dev1
Updating b3c73e0..9ff7b27
Fast-forward
 merge.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\mergeconflict> git merge dev2
Auto-merging merge.py
CONFLICT (content): Merge conflict in merge.py
Automatic merge failed; fix conflicts and then commit the result.
PS F:\Euron\GitHub\gitlearn\mergeconflict> 

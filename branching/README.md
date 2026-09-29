Branching and Feature Development

Create a project with a main branch and at least three feature branches: feature-login, feature-profile, and feature-dashboard. Implement a small change in each branch and merge all three features into main.

Sample Input:

mkdir branching
cd branching

# Initialize Git repository
git init -b main

git add test.py
git commit -m "Initial commit"

# Create and switch to the feature-login branch
git checkout -b feature-login

# Stage and commit the change
git add test.py
git commit -m "Feature login"

# Return to the main branch 
git checkout main

# Merge the login feature
git merge feature-login

# Create and switch to the feature-profile branch
git checkout -b feature-profile

# Stage and commit the change
git add test.py
git commit -m "Feature profile"

# Return to the main branch 
git checkout main

# Merge the login feature
git merge feature-profile

# Create and switch to the feature-dashboard branch
git checkout -b feature-dashboard

# Stage and commit the change
git add test.py
git commit -m "Feature dashboard"

# Return to the main branch 
git checkout main

# Merge the login feature
git merge feature-dashboard

# Branch deletion
git branch -d feature-login
git branch -d feature-profile
git branch -d feature-dashboard

# Git history
git log --oneline --graph --decorate --all

Sample Output:

PS F:\Euron\GitHub\gitlearn> mkdir branching


    Directory: F:\Euron\GitHub\gitlearn


Mode                 LastWriteTime         Length Name                                                                                            
----                 -------------         ------ ----                                                                                            
d-----        29-09-2026     15:16                branching                                                                                       


PS F:\Euron\GitHub\gitlearn> cd .\branching\
PS F:\Euron\GitHub\gitlearn\branching> git init -b main
Initialized empty Git repository in F:/Euron/GitHub/gitlearn/branching/.git/
PS F:\Euron\GitHub\gitlearn\branching> git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
PS F:\Euron\GitHub\gitlearn\branching> git add .\test.py
PS F:\Euron\GitHub\gitlearn\branching> git commit -m "Initial commit"
[main (root-commit) 4f5e362] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 test.py
PS F:\Euron\GitHub\gitlearn\branching> git branch
* main
PS F:\Euron\GitHub\gitlearn\branching> git status 
On branch main
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\branching> git checkout -b feature-login
Switched to a new branch 'feature-login'
PS F:\Euron\GitHub\gitlearn\branching> git branch
* feature-login
  main
PS F:\Euron\GitHub\gitlearn\branching> git add .\test.py
PS F:\Euron\GitHub\gitlearn\branching> git commit -m "Feature login" 
[feature-login 378f7cd] Feature login
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\branching> git status
On branch feature-login
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\branching> git checkout main
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\branching> git checkout feature-login
Switched to branch 'feature-login'
PS F:\Euron\GitHub\gitlearn\branching> git branch
* feature-login
  main
PS F:\Euron\GitHub\gitlearn\branching> git checkout main         
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\branching> git merge feature-login
Updating 4f5e362..378f7cd
Fast-forward
 test.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\branching> git branch
  feature-login
* main
PS F:\Euron\GitHub\gitlearn\branching> git checkout -b feature-profile
Switched to a new branch 'feature-profile'
PS F:\Euron\GitHub\gitlearn\branching> git status                     
On branch feature-profile
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.py

no changes added to commit (use "git add" and/or "git commit -a")
PS F:\Euron\GitHub\gitlearn\branching> git add .\test.py              
PS F:\Euron\GitHub\gitlearn\branching> git commit -m "Feature profile"
[feature-profile 449400e] Feature profile
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\branching> git status                     
On branch feature-profile
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\branching> git checkout main              
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\branching> git merge feature-profile      
Updating 378f7cd..449400e
Fast-forward
 test.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\branching> git checkout -b feature-dashboard
Switched to a new branch 'feature-dashboard'
PS F:\Euron\GitHub\gitlearn\branching> git add .\test.py                
PS F:\Euron\GitHub\gitlearn\branching> git commit -m "Feature dashboard"
[feature-dashboard 87fd94d] Feature dashboard
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\branching> git status                       
On branch feature-dashboard
nothing to commit, working tree clean
PS F:\Euron\GitHub\gitlearn\branching> git checkout main                
Switched to branch 'main'
PS F:\Euron\GitHub\gitlearn\branching> git merge feature-dashboard      
Updating 449400e..87fd94d
Fast-forward
 test.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
PS F:\Euron\GitHub\gitlearn\branching> git log --oneline
87fd94d (HEAD -> main, feature-dashboard) Feature dashboard
449400e (feature-profile) Feature profile
378f7cd (feature-login) Feature login
4f5e362 Initial commit
PS F:\Euron\GitHub\gitlearn\branching> git log --oneline --graph --decorate --all
* 87fd94d (HEAD -> main, feature-dashboard) Feature dashboard
* 449400e (feature-profile) Feature profile
* 378f7cd (feature-login) Feature login
* 4f5e362 Initial commit
PS F:\Euron\GitHub\gitlearn\branching> git branch -d feature-login               
Deleted branch feature-login (was 378f7cd).
PS F:\Euron\GitHub\gitlearn\branching> git branch                                
  feature-dashboard
  feature-profile
* main
PS F:\Euron\GitHub\gitlearn\branching> git branch -d feature-profile
Deleted branch feature-profile (was 449400e).
PS F:\Euron\GitHub\gitlearn\branching> git branch                   
  feature-dashboard
* main
PS F:\Euron\GitHub\gitlearn\branching> git branch -d feature-dashboard           
Deleted branch feature-dashboard (was 87fd94d).
PS F:\Euron\GitHub\gitlearn\branching> git branch                     
* main
PS F:\Euron\GitHub\gitlearn\branching> git log --oneline --graph --decorate --all
* 87fd94d (HEAD -> main) Feature dashboard
* 449400e Feature profile
* 378f7cd Feature login
* 4f5e362 Initial commit
PS F:\Euron\GitHub\gitlearn\branching> 

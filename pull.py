#!/usr/local/bin/python3
__author__ = 'Jeremiahgibson91 & James & Jared(thang1thang2)'
# Windows ONLY (SORRY OTHERS - USE WINDOWS - TOO LAZY)
# Pull students repositories
#
# --- SETUP ---
# Download and install msysgit >> https://msysgit.github.io/
# Open CMD as administrator
# $ C:\Python34\scripts\pip install github3.py
#
# Make sure to add to your path (64-bit PC):
# C:\Program Files (x86)\Git\bin
# 32-bit PC's
# C:\Program Files\Git\bin
#
# --- RUN IT ---
# Open CMD
# $ C:\Python34\python C:\PATH\TO\SCRIPT\pull.py
##
import os
import github3
import subprocess
import shutil

# username, password
login = ['username','password']
path = 'students'

if __name__ == '__main__':
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    os.chdir(path)

    g = github3.login(login[0], login[1])

    for repo in g.iter_repos(type='collaborator'):
        repo_parts = repo.clone_url.split('//')
        url=repo_parts[0]+'//'+login[0]+':'+login[1]+'@'+repo_parts[1]
        #print(url)
        subprocess.call(['git', 'clone',url])
        # If windows => path; else assume sane unix path
    print('DONE')

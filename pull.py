# #!/usr/local/bin/python3
__author__ = 'Jeremiahgibson91 & James'
# Windows ONLY (SORRY OTHERS - USE WINDOWS - TOO LAZY)
# Pull students repositories
#
# --- SETUP ---
# Download and install msysgit >> https://msysgit.github.io/
# Open CMD as administrator
# $ C:\Python34\scripts\pip install github3.py
#
# --- RUN IT ---
# Open CMD
# $ C:\Python34\python C:\PATH\TO\SCRIPT\pull.py
##
import os
import github3
import subprocess
import shutil

login = 'thang1thang2:class_g15'
path = '/Volumes/Mavericks/Users/jaredweakly/Documents/Classes/Grading/students'

if __name__ == '__main__':
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    os.chdir(path)

    g = github3.login('thang1thang2', 'class_g15')

    for repo in g.iter_repos(type='collaborator'):
        yolo = repo.clone_url.split('//')
        subprocess.call(['git', 'clone',yolo[0]+'//'+login+'@'+yolo[1]])
        #subprocess.call(['C:\\Program Files (x86)\\Git\\bin\\git', 'clone', repo.clone_url])
        # If windows => path; else assume sane unix path
    print('DONE')

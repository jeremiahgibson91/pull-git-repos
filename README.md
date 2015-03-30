# Pull-Git-Repos

The intent of this python script is to allow users to pull all associated Repositories to the user account attached to this script. This script will check to see if the folder you want to save the repos at exists; if it does it deletes it and adds a new folder in its place, cloning all associated repos into the new folder.This keeps all repo's up-to-date and prevents a few file associated errors.

# Requirements

Pull-git-repos depends on the modules:

* [os](https://docs.python.org/3.4/library/os.html)
* [github3](https://github3py.readthedocs.org/en/master/)
* [subprocess](https://docs.python.org/3.4/library/subprocess.html)
* [shutil](https://docs.python.org/3.4/library/shutil.html)

import glob
import os
import sys

# Get the directory name
if sys.platform == 'Win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']


path = '/Users/paddyweezy/Documents/pycharm_projects/exercise10'

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames

print(glob.glob('**/*.py', recursive=True))

# TODO: use os.path.getsize to find each file's size
Size = os.path.getsize(path)
# print(os.path.getsize(path))
print(Size)

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

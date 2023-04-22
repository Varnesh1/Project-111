import os,shutil

from_dir = 'Document_Files'
to_dir = 'move_file.py'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
   tu,ou = os.path.splitext('skj.py')
   
print(tu,ou)    
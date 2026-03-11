import os
directory_path = '/Windows/System32'
contents = os.listdir(directory_path)
for item in contents:    print(item)
#print(contents)
'''this program is yused to print ha list of files and directories in the specified directory path. 
In this case, it will print the contents of the root directory ('/'). 
You can change the 'directory_path' variable to any other directory you want to explore.  '''
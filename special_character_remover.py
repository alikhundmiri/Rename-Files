#change the names of given files
import os

directory = ""
##change the Directory here in the 2 lines below
file_list = os.listdir (r"DIRECTORY HERE")
os.chdir(r"DIRECTORY HERE")
for list in file_list:
    new_text =  list.strip("WHAT DO YOU WANT TO REMOVE")
    os.rename(list,new_text)
    print(new_text)

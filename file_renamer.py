import os

##change the Directory here in the 2 lines below
directory = ""
file_list = os.listdir (r"/Users/alikhundmiri/Documents/Tutorials/Python_Scrapping")
os.chdir(r"/Users/alikhundmiri/Documents/Tutorials/Python_Scrapping")
for list in file_list:
    #print (list)
    new_text =  list.strip("Your Text here")
    os.rename(list,new_text)
    print(new_text)


import os

def rename1():
    list1= os.listdir(r"C:\Users\solan\Desktop\prog nano\IPND_materials\4-Create-a-Movie-Website\1_using_functions\b_secret_message\prank")
    saved_path=os.getcwd()
    print(list1)
    os.chdir(r"C:\Users\solan\Desktop\prog nano\IPND_materials\4-Create-a-Movie-Website\1_using_functions\b_secret_message\prank")
    for name in list1:
        os.rename(name, ''.join([i for i in name if not i.isdigit()]))
    os.chdir(saved_path)

rename1()

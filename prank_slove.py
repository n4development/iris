import os

image_dir = os.curdir+'/prank/prank/'
file_list = os.listdir(image_dir)
for file in file_list:
    print(file+'\n')
    file_full_path = image_dir+file
    new_name = file.translate(None,"1234567890")
    os.rename(file_full_path,image_dir+new_name)
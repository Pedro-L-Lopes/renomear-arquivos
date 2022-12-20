import os 

folder = r'folder path\\'

i=0
for file_name in os.listdir(folder):
    old_name = folder + file_name
    i+=1
    new_name = folder + f'new name here{i}.jpg' + file_name
    os.rename(old_name, new_name)

print(os.listdir(folder))
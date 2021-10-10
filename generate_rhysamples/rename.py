import os

path = 'C:/DataBaker_songs/ph_for_rhy'
files=os.listdir(path)
for file in files:
    content = file.split('_')
    new_name = content[0] + '_' + content[1][0:3] + '_' + content[1][3:] + '.pitch'
    os.rename(path + os.sep + file,path + os.sep +new_name)

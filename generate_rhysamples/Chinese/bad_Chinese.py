import os
from toolbox_Chinese.deletenotescut import delete_files
from toolbox_Chinese.cutandchange import cutandchange
from toolbox_Chinese.merge import merge_files
# from toolbox_Chinese.change import change
# from toolbox_Chinese.together import together
from toolbox_Chinese.estimate_picth import *
from test import together

# The most primitive path
ori_path = 'C:/DataBaker_songs'
singer_names = ['DB-DM-001-F-001','DB-DM-002-F-002','DB-DM-003-F-003','DB-DM-004-M-001',
'DB-DM-005-M-002','DB-DM-006-F-004','DB-DM-007-M-003','DB-DM-008-M-004']
# singer_names = [ 'DB-DM-005-M-002']

# creat file for bad samples
for singer_name in singer_names:
    if not os.path.exists(ori_path + os.sep + singer_name + '/badsample_changerhythm'):
        os.makedirs(ori_path + os.sep + singer_name + '/badsample_changerhythm')

# read song names
for singer_name in singer_names:
    second_path = ori_path + os.sep + singer_name + os.sep + 'Vox'
    f_list = os.listdir(second_path)
    Vox_list = []
    for f in f_list:
        if os.path.splitext(f)[1] == '.wav':  # seperate with extension name
            Vox_list.append(f.split('.')[0])
    # generate mapping list
    # Vox_list = ['041']
    for song_name in Vox_list:
        print((singer_name,song_name))
        # together(ori_path + os.sep + singer_name, song_name)


        # delete_files(ori_path,singer_name,song_name)
        # cutandchange(ori_path + os.sep + singer_name, song_name)

        # merge
        # merge_files(ori_path + os.sep + singer_name, song_name)

        # ph
        runph(ori_path + os.sep + singer_name, song_name,singer_name)
        # runph(ori_path + os.sep + singer_name, song_name)

        # delete
        # delete_files(ori_path,singer_name,song_name)


        # plot
        # plotph(ori_path + os.sep + singer_name + os.sep + 'badsample_changepitch' + os.sep + song_name + os.sep + 'pitch.pitch' )




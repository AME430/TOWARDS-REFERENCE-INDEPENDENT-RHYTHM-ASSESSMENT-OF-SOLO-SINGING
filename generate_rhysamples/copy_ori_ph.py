import os
import shutil

ori_path1 = 'C:/DataBaker_songs'
singer_names1 = ['DB-DM-001-F-001','DB-DM-002-F-002','DB-DM-003-F-003','DB-DM-004-M-001',
                 'DB-DM-005-M-002','DB-DM-006-F-004','DB-DM-007-M-003','DB-DM-008-M-004']

for singer_name in singer_names1:
    print(singer_name)
    second_path = ori_path1 + os.sep + singer_name + os.sep + 'Vox'
    f_list = os.listdir(second_path)
    Vox_list = []
    for f in f_list:
        if os.path.splitext(f)[1] == '.wav':  # seperate with extension name
            Vox_list.append(f.split('.')[0])
    label_list =['_ori']

    for song_name in Vox_list:
        for label in label_list:
            old_file_ori = ori_path1 +os.sep + '400_correct_ph_pitch' + os.sep + singer_name + '_' + song_name + label + '.pitch'
            new_file_path1= 'C:/DataBaker_songs/ph_for_rhy/' + singer_name + '_' + song_name + label +'.pitch'
            shutil.copyfile(old_file_ori,new_file_path1)

import  os
import shutil

# # copy Mandarin
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

    # label_list =['_ori','_0','_1','_2','_3','_4','_speech_snippet']
    label_list =['_ori']

    for song_name in Vox_list:
        for label in label_list:
            old_file_ori = ori_path1 +os.sep + '400_correct_ph_sni' + os.sep + singer_name + '_' + song_name + label + '.wav'
            new_file_path1= 'C:/DataBaker_songs/rhy_sni/' + singer_name + '_' + song_name + label +'.wav'
            shutil.copyfile(old_file_ori,new_file_path1)
        rhy_list = os.listdir(ori_path1 +os.sep +singer_name +os.sep + 'badsample_changerhythm' + os.sep + song_name )
        for file in rhy_list:
            if os.path.splitext(file)[1] == '.wav' and file.split('.')[1].split('_')[1]=='sni':  # seperate with extension name
                old_file = ori_path1 +os.sep +singer_name +os.sep + 'badsample_changerhythm' + os.sep + song_name +os.sep + file
                new_file_path2= 'C:/DataBaker_songs/rhy_sni/' + singer_name + '_' + song_name + '_' + file.split('_')[0] +'.wav'
                shutil.copyfile(old_file ,new_file_path2)

##############################
# ori_path = 'C:/Dataset/NHSS_Database/Data'
# singer_names = ['F01','F02','F03','F04','F05','M01','M02','M03','M04','M05']
#
# for singer_name in singer_names:
#     print(singer_name)
#     second_path = ori_path + os.sep + singer_name
#     f_list = os.listdir(second_path)
#     song_names = []
#
#     for f in f_list:
#         if f.startswith('S'):
#             song_names.append(f)
#
#     # label_list =['_ori','_0','_1','_2','_3','_4','_speech_snippet']
#     label_list =['_ori','_2','_speech_snippet']
#     for song_name in song_names:
#         for label in label_list:
#             old_file_ori = ori_path +os.sep + singer_name + os.sep + song_name+os.sep + 'badsample_400_exp1' + os.sep + 'result' + os.sep + song_name + label + '.wav'
#             new_file_path1= 'C:/DataBaker_songs/snippet_onlypitchchange/' + singer_name + '_' + song_name + label +'.wav'
#             shutil.copyfile(old_file_ori,new_file_path1)
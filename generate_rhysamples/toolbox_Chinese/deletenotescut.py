import os
import shutil
# from toolbox_Chinese.merge import merge_files
# from toolbox_Chinese.estimate_picth import *


def delete_files(ori_path,singer_name,song_name):

    delete_path = ori_path + os.sep + singer_name + os.sep + 'badsample_changerhythm' + os.sep + song_name +os.sep
    delete_file1 = 'nosilence.wav'
    # delete_file2 = 'small.wav'
    # delete_file3 ='speech_' + song_name +'.wav'
    delete_dir1 = 'notescut'

    if os.path.exists(delete_path + delete_file1):
        os.remove(delete_path + delete_file1)
    # if os.path.exists(delete_path + delete_file2):
    #     os.remove(delete_path +delete_file2)
    # if os.path.exists(delete_path + delete_file3):
    #     os.remove(delete_path +delete_file3)
    if os.path.exists(delete_path + delete_dir1):
        shutil.rmtree(delete_path + delete_dir1)

    ###################################################
    # ori_path = 'C:/Dataset/NHSS_Database/Data'
    # singer_names = ['F01','F02','F03','F04','F05','M01','M02','M03','M04','M05']
    #
    # for singer_name in singer_names:
    #     second_path = ori_path + os.sep + singer_name
    #     f_list = os.listdir(second_path)
    #     song_names = []
    #
    #     for f in f_list:
    #         if f.startswith('S'):
    #             song_names.append(f)
    #
    #     for song_name in song_names:
    #         delete_path = ori_path + os.sep + singer_name + os.sep + song_name +os.sep
    #         delete_file1 = 'song_nosilence.wav'
    #         delete_file2 = 'small.wav'
    #         delete_file3 ='speech.wav'
    #
    #         if os.path.exists(delete_path + delete_file1):
    #             os.remove(delete_path + delete_file1)
    #         if os.path.exists(delete_path + delete_file2):
    #             os.remove(delete_path +delete_file2)
    #         if os.path.exists(delete_path + delete_file3):
    #             os.remove(delete_path +delete_file3)




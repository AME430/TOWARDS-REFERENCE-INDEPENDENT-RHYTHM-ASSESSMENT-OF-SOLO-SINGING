import os
import sys
sys.path.append('/home/chitra/workspace/code/JinhuLi/exp_onlyrh')
import pdb
import scipy.io.wavfile
import dill
from hybrid_CRNN.create_data.pitch_histogram import CreateNoteHistogram
from matplotlib import pylab as plt
import numpy as np
import librosa
import wave
import random


def CreateBWSdict(bwsfile):
    ## This function takes in bws file and outputs a dictionary with the singername and the corresponding score
    flines = open(bwsfile, 'r').readlines()
    names_scores = []
    for line in flines:
        name, score = line.replace('\n', '').split(',')
        names_scores.append((name, float(score)))
    names_scores.sort(key=lambda x: (-x[1], x[0]))
    SingerScore = {}
    for name, score in names_scores:
        SingerScore[name] = score
    return names_scores, SingerScore


def plotpitch(pitch):
    plt.figure()
    plt.plot(pitch)
    plt.show()

mother_dir1 = '/home/chitra/workspace/code/JinhuLi/rhypaper_twosongs/'
# singer_names1 = ['DB-DM-001-F-001','DB-DM-002-F-002','DB-DM-003-F-003','DB-DM-004-M-001',
#                  'DB-DM-005-M-002','DB-DM-006-F-004','DB-DM-007-M-003','DB-DM-008-M-004',
#                  'F01','F02','F03','F04','F05','M01','M02','M03','M04','M05']




if not os.path.exists('/home/chitra/workspace/code/JinhuLi/dill_papertwosongs'):
    os.makedirs('/home/chitra/workspace/code/JinhuLi/dill_papertwosongs')
cv1_folder = '/home/chitra/workspace/code/JinhuLi/dill_papertwosongs'
#train_dill = open(cv1_folder + os.sep + 'train_1.dill', 'wb')
test_dill = open(cv1_folder + os.sep + 'test_1.dill', 'wb')
#val_dill = open(cv1_folder + os.sep + 'val_1.dill', 'wb')

#train_tobedumped = []
test_tobedumped = []
#val_tobedumped = []

bwsfile1 = mother_dir1 + os.sep + 'bws.txt'
# bwsfile2 = mother_dir2 + os.sep + 'bws_file.txt'
### Create dictionary of Human BWS Scores
singer_score_tuple_sorted1, singer_score_dict1 = CreateBWSdict(bwsfile1)
random.shuffle(singer_score_tuple_sorted1)
# singer_score_tuple_sorted2, singer_score_dict2 = CreateBWSdict(bwsfile2)

for idx in range(20):
    label = singer_score_tuple_sorted1[idx][0] # label == singername+_+songname
    #print(label)
    rating = singer_score_tuple_sorted1[idx][1]
    singer_name = label.split('_')[0]
    song_name = label.split('_')[1]
    print((singer_name,song_name))

    wavfile1 = mother_dir1 + os.sep +  'wav_sni' + os.sep + singer_name + '_' + song_name + '.wav'
    #original_pitch_file = pitch_folder + os.sep + singer_name + '_' + song_name + '_' + rhy_rate +'.pitch'
    rhythm_his = mother_dir1 + os.sep +  'rh' + os.sep + singer_name + '_' + song_name+ '.txt'
    rh_list = []
    f = open(rhythm_his,"r") 
    lines = f.readlines()     
    for line in lines:
      rh_list.append(eval(line))


    audio,fs= librosa.load(wavfile1,sr=None)
    #ph_notes = CreateNoteHistogram(original_pitch_file)
    # rating = random.random()
    test_tobedumped.append({'audio': [audio,fs],'pitch_histogram': rh_list, 'ratings': [(rating-3)/2]})
    print((rating-3)/2)

dill.dump(test_tobedumped, test_dill)


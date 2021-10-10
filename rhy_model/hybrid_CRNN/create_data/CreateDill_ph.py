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

mother_dir1 = '/home/chitra/workspace/code/JinhuLi'
# singer_names1 = ['DB-DM-001-F-001','DB-DM-002-F-002','DB-DM-003-F-003','DB-DM-004-M-001',
#                  'DB-DM-005-M-002','DB-DM-006-F-004','DB-DM-007-M-003','DB-DM-008-M-004',
#                  'F01','F02','F03','F04','F05','M01','M02','M03','M04','M05']

# mother_dir2 = 'C:/Dataset/NHSS_Database/Data'
# singer_names2 = ['F01','F02','F03','F04','F05','M01','M02','M03','M04','M05']

pitch_folder =  mother_dir1 + os.sep +  'ph_for_rhy'

test_singers = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
                201,211,221,231,241,251,261,271,281,291,301,311,321,331,341,351,361,371,381,391,401,411,421,431,441,451,461,471,481,491]
val_singers = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192,
               202,212,222,232,242,252,262,272,282,292,302,312,322,332,342,352,362,372,382,392,402,412,422,432,442,452,462,472,482,492]
train_singers = list(set(range(500)) - set(test_singers) - set(val_singers))


if not os.path.exists('/home/chitra/workspace/code/JinhuLi/dill_onlyrh'):
    os.makedirs('/home/chitra/workspace/code/JinhuLi/dill_onlyrh')
cv1_folder = '/home/chitra/workspace/code/JinhuLi/dill_onlyrh'
train_dill = open(cv1_folder + os.sep + 'train_1.dill', 'wb')
test_dill = open(cv1_folder + os.sep + 'test_1.dill', 'wb')
val_dill = open(cv1_folder + os.sep + 'val_1.dill', 'wb')

train_tobedumped = []
test_tobedumped = []
val_tobedumped = []

bwsfile1 = mother_dir1 + os.sep + 'bws_rhy.txt'
# bwsfile2 = mother_dir2 + os.sep + 'bws_file.txt'
### Create dictionary of Human BWS Scores
singer_score_tuple_sorted1, singer_score_dict1 = CreateBWSdict(bwsfile1)
random.shuffle(singer_score_tuple_sorted1)
# singer_score_tuple_sorted2, singer_score_dict2 = CreateBWSdict(bwsfile2)

for idx in train_singers:
    label = singer_score_tuple_sorted1[idx][0] # label == singername+_+songname
    #print(label)
    rating = singer_score_tuple_sorted1[idx][1]
    singer_name = label.split('_')[0]
    song_name = label.split('_')[1]
    rhy_rate = label.split('_')[2]
    print((singer_name,song_name))

    wavfile1 = mother_dir1 + os.sep +  'rhy_sni' + os.sep + singer_name + '_' + song_name + '_' + rhy_rate + '.wav'
    original_pitch_file = pitch_folder + os.sep + singer_name + '_' + song_name + '_' + rhy_rate +'.pitch'
    rhythm_his = mother_dir1 + os.sep +  'rh_folder' + os.sep + singer_name + '_' + song_name + '_' + rhy_rate + '.txt'
    rh_list = []
    f = open(rhythm_his,"r") 
    lines = f.readlines()     
    for line in lines:
      rh_list.append(eval(line))


    audio,fs= librosa.load(wavfile1,sr=None)
    #ph_notes = CreateNoteHistogram(original_pitch_file)
    # rating = random.random()
    train_tobedumped.append({'audio': [audio,fs], 'pitch_histogram': rh_list, 'ratings': [rating]})

for idx in test_singers:
    label = singer_score_tuple_sorted1[idx][0] # label == singername+_+songname
    rating = singer_score_tuple_sorted1[idx][1]
    singer_name = label.split('_')[0]
    song_name = label.split('_')[1]
    rhy_rate = label.split('_')[2]
    print((singer_name,song_name))

    wavfile1 = mother_dir1 + os.sep +  'rhy_sni' + os.sep + singer_name + '_' + song_name + '_' + rhy_rate + '.wav'
    original_pitch_file = pitch_folder + os.sep + singer_name + '_' + song_name + '_' + rhy_rate +'.pitch'
    rhythm_his = mother_dir1 + os.sep +  'rh_folder' + os.sep + singer_name + '_' + song_name + '_' + rhy_rate + '.txt'
    rh_list = []
    f = open(rhythm_his,"r") 
    lines = f.readlines()     
    for line in lines:
      rh_list.append(eval(line))
    
    
    audio,fs = librosa.load(wavfile1,sr = None)
    #ph_notes = CreateNoteHistogram(original_pitch_file)
    # rating = random.random()
    test_tobedumped.append({'audio': [audio, fs], 'pitch_histogram': rh_list, 'ratings': [rating]})

for idx in val_singers:
    label = singer_score_tuple_sorted1[idx][0] # label == singername+_+songname
    rating = singer_score_tuple_sorted1[idx][1]
    singer_name= label.split('_')[0]
    song_name = label.split('_')[1]
    rhy_rate = label.split('_')[2]
    print((singer_name,song_name))

    wavfile1 = mother_dir1 + os.sep +  'rhy_sni' + os.sep + singer_name + '_' + song_name + '_' + rhy_rate + '.wav'
    original_pitch_file = pitch_folder + os.sep + singer_name + '_' + song_name + '_' + rhy_rate +'.pitch'
    rhythm_his = mother_dir1 + os.sep +  'rh_folder' + os.sep + singer_name + '_' + song_name + '_' + rhy_rate + '.txt'
    rh_list = []
    f = open(rhythm_his,"r") 
    lines = f.readlines()     
    for line in lines:
      rh_list.append(eval(line))

    audio,fs= librosa.load(wavfile1,sr=None)
    # rating = random.random()
    
    
    #ph_notes = CreateNoteHistogram(original_pitch_file)
    val_tobedumped.append({'audio': [audio, fs], 'pitch_histogram': rh_list, 'ratings': [rating]})

dill.dump(train_tobedumped, train_dill)
dill.dump(test_tobedumped, test_dill)
dill.dump(val_tobedumped, val_dill)

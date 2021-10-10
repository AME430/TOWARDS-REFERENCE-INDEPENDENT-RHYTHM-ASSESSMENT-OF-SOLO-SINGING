import os
import re
import librosa



def cutandchange(path,song_name):
    # PATH = 'C:/DataBaker_songs/DB-DM-001-F-001'
    song_interval_path = path + os.sep + 'interval'

    with open(song_interval_path + os.sep + song_name + '.interval') as file:
        lines = file.readlines()
        lines = lines[12:-1] # delete some lines at start
        label = 0
        mid = []
        phoneme_sing = []
        for line in lines:
            if label == 2:
                mid.append(line.split('"')[1])
            else:
                mid.append(eval(line))
            label = label + 1
            if label == 3:
                label = 0
                mid[1] = mid[1] - mid[0]
                phoneme_sing.append(mid)
                mid = []

    starttime = []
    duration = []
    for phone in phoneme_sing:
        starttime.append(phone[0])
        duration.append(phone[1])

    if not os.path.exists(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'notescut'):
        os.makedirs(path +  os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'notescut')

    y, sr = librosa.load(path + os.sep + 'Vox' + os.sep + song_name + '.wav' ,sr=None)
    f = song_name + '.wav'
    for i in range(len(starttime)):
        point1 = int(starttime[i] * sr)
        point2 = int((starttime[i]+duration[i])*sr)
        b = y[point1:point2]
        librosa.output.write_wav(path + '/badsample_changerhythm/' + song_name + os.sep + 'notescut' + os.sep + str(i + 1) + "_" + f, b,sr)
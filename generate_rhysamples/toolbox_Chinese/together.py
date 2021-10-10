import os
import numpy as np
import librosa
from pydub import AudioSegment
import random


def together(path,song_name):
    # PATH = 'C:/DataBaker_songs/DB-DM-001-F-001'
    song_interval_path = path + os.sep + 'interval'

    with open(song_interval_path + os.sep + song_name + '.interval') as file:
        lines = file.readlines()
        lines = lines[12:] # delete some lines at start
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

    path_read_folder = path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'notescut'

    files= []
    for f in os.listdir(path_read_folder):
        files.append(f)

    files.sort(key = lambda x: int(x[:-8]))

    merged_signal = []
    scale = 0.5

    if not os.path.exists(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'info'):
        os.mkdir(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'info')

    head = []
    content = []
    file = open(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'info' + os.sep + str(scale) + '.interval','w')
    timeline = 0
    ori_timeline = 0
    for i in range(len(files)):
        if os.path.exists(path_read_folder + os.sep + str(i+1) + "_" + song_name + ".wav"):
            if i == 0:
                b,sr = librosa.load(path_read_folder + os.sep + str(i+1) + "_" + song_name + ".wav",sr=None)
                merged_signal.append(b)
                line1 = phoneme_sing[i][0]
                content.append(str(line1))
                # file.write(str(line1))
                # file.write('\n')
                line2 = phoneme_sing[i][1]
                content.append(str(line2))
                # file.write(str(line2))
                # file.write('\n')
                line3 = phoneme_sing[i][2]
                content.append('"'+line3 + '"')
                # file.write(line3)
                # file.write('\n')
                timeline = timeline + line2
                ori_timeline = ori_timeline + line2
            else:
                signal1,sr = librosa.load(path_read_folder + os.sep + str(i+1) + "_" + song_name + ".wav",sr=None)
                rate = random.uniform(1 - scale,1+scale)
                b = librosa.effects.time_stretch(signal1,rate=rate)
                merged_signal.append(b)

                distancetime = phoneme_sing[i][0] - ori_timeline
                ori_timeline = ori_timeline + distancetime
                timeline = timeline + distancetime
                line1 =  timeline
                content.append(str(line1))
                # file.write(str(line1))
                # file.write('\n')
                line2 = phoneme_sing[i][1]
                ori_timeline = ori_timeline + line2
                timeline = timeline + line2 * rate
                content.append(str(line1))
                # file.write(str(timeline))
                # file.write('\n')
                line3 = phoneme_sing[i][2]
                content.append('"'+line3 + '"')
                # file.write(line3)
                # file.write('\n')
    file.close()
    sr = 48000
    path_write_wav_file = path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + str(scale) + '_small.wav'
    merged_signal = np.hstack(merged_signal)
    merged_signal = np.asarray(merged_signal, dtype=np.float32)
    # merged_signal = np.asarray(merged_signal)
    librosa.output.write_wav(path_write_wav_file, merged_signal,sr)
    # print(librosa.__version__)
    # print(numba.__version__)


    # louder
    song = AudioSegment.from_wav(path_write_wav_file)

    song = song + 10

    song.export(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + str(scale) + 'result.wav', "wav")
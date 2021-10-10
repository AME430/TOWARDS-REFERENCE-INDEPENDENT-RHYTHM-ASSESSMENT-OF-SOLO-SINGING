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

    total_n = len( starttime)
    division_ratio = 10

    snippet_length = total_n//division_ratio

    if not os.path.exists(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'notescut'):
        os.makedirs(path +  os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'notescut')

    y, sr = librosa.load(path + os.sep + 'Vox' + os.sep + song_name + '.wav' ,sr=None)
    f = song_name + '.wav'

    scale_list = [0.2,0.4,0.6,0.8]
    for scale in scale_list:
        scale = scale + random.gauss(0,0.05) #####################################################
        merged_signal = []
        if not os.path.exists(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'info'):
            os.mkdir(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'info')
        file = open(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'info' + os.sep + str(round(scale,3)) + '.interval','w')

        head = []
        content = []
        timeline = 0
        ori_timeline = 0

        left = (4)*snippet_length
        right = (5)*snippet_length

        for i in range(len(starttime)):
            if i == 0:
                point1 = int(starttime[i] * sr)
                point2 = int((starttime[i]+duration[i])*sr)
                b = y[point1:point2]
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
                point1 = int(starttime[i] * sr)
                point2 = int((starttime[i]+duration[i])*sr)
                signal1 = y[point1:point2]
                rate = random.uniform(1 - scale,1+scale)
                b = librosa.effects.time_stretch(signal1,rate=rate)
                merged_signal.append(b)

                distancetime = starttime[i] - ori_timeline
                ori_timeline = ori_timeline + distancetime
                timeline = timeline + distancetime
                line1 =  timeline
                content.append(str(line1))
                # file.write(str(line1))
                # file.write('\n')
                line2 = duration[i]
                ori_timeline = ori_timeline + line2
                timeline = timeline + line2/rate
                content.append(str(timeline))
                # file.write(str(timeline))
                # file.write('\n')
                line3 = phoneme_sing[i][2]
                content.append('"'+line3 + '"')
                # file.write(line3)
                # file.write('\n')

        merged_signal_sni = []
        for i in range(left,right):
            if i == 0:
                point1 = int(starttime[i] * sr)
                point2 = int((starttime[i]+duration[i])*sr)
                b = y[point1:point2]
                merged_signal_sni.append(b)

            else:
                point1 = int(starttime[i] * sr)
                point2 = int((starttime[i]+duration[i])*sr)
                signal1 = y[point1:point2]
                rate = random.uniform(1 - scale,1+scale)
                b = librosa.effects.time_stretch(signal1,rate=rate)
                merged_signal_sni.append(b)

        # file.close()
        part_head1 = ['File type = "ooTextFile"','Object class = "TextGrid"','\n']
        part_head2 = ['<exists>','1','"IntervalTier"','"04"']
        part_head3 = ['0',str(timeline)]
        head.extend(part_head1)
        head.extend(part_head3)
        head.extend(part_head2)
        head.extend(part_head3)
        head.append(str(len(content)/3))

        for ctx in head:
            file.write(ctx)
            if ctx != '\n':
                file.write('\n')

        for ctx in content:
            file.write(ctx)
            file.write('\n')

        file.close()
        sr = 48000
        path_write_wav_file = path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + str(round(scale,3)) + '_full.wav'
        merged_signal = np.hstack(merged_signal)
        merged_signal = np.asarray(merged_signal, dtype=np.float32)
        librosa.output.write_wav(path_write_wav_file, merged_signal,sr)

        path_write_wav_file = path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + str(round(scale,3)) + '_sni.wav'
        merged_signal_sni = np.hstack(merged_signal_sni)
        merged_signal_sni = np.asarray(merged_signal_sni, dtype=np.float32)
        librosa.output.write_wav(path_write_wav_file, merged_signal_sni,sr)

        # louder
        # song = AudioSegment.from_wav(path_write_wav_file)
        #
        # song = song + 10
        #
        # song.export(path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + str(scale) + 'result.wav', "wav")
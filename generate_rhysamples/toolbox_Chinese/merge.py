import os
import glob
import numpy as np
import scipy.io.wavfile as wav
import librosa
from pydub import AudioSegment
import random
import numpy
import numba

def merge_files(path,song_name):
    path_read_folder = path + os.sep + 'badsample_changerhythm' + os.sep + song_name + os.sep + 'notescut'

    files= []
    for f in os.listdir(path_read_folder):
        files.append(f)

    files.sort(key = lambda x: int(x[:-8]))

    merged_signal = []
    scale = 0.5
    for i in range(len(files)):
        if os.path.exists(path_read_folder + os.sep + str(i+1) + "_" + song_name + ".wav"):
            signal1,sr = librosa.load(path_read_folder + os.sep + str(i+1) + "_" + song_name + ".wav",sr=None)
            rate = random.uniform(1 - scale,1+scale)
            b = librosa.effects.time_stretch(signal1,rate=rate)
            merged_signal.append(b)
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





import os

bws_path = 'C:/DataBaker_songs/bws_rhy_2.txt'
with open(bws_path,'w') as f:
    file_list = os.listdir('C:/DataBaker_songs/rhy_sni' )
    for file in file_list:
        content = file.split('_')
        singer_name = content[0]
        song_name = content[1]
        label = content[2].split('.')
        if len(label) == 2:
            line = singer_name + '_' + song_name + '_'+ label[0] + ',1'
            f.write(line)
            f.write('\n')
        else:
            rate = eval(label[0]+'.'+label[1])
            gt = -2*rate +1
            line = singer_name + '_' + song_name+ '_' + label[0] +'.'+label[1] + ',' + str(round(gt,3))
            f.write(line)
            f.write('\n')

f.close()

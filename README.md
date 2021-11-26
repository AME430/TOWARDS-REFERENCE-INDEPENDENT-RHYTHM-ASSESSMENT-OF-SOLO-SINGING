# Introduction
These codes are for the paper -- TOWARDS REFERENCE-INDEPENDENT RHYTHM ASSESSMENT OF SOLO SINGING

[generate_rhysamples](https://github.com/AME430/TOWARDS-REFERENCE-INDEPENDENT-RHYTHM-ASSESSMENT-OF-SOLO-SINGING/tree/master/generate_rhysamples "generate_rhysamples") is used for generating different rhythm performance samples. You can use it by running [bad_Chinese.py](https://github.com/AME430/TOWARDS-REFERENCE-INDEPENDENT-RHYTHM-ASSESSMENT-OF-SOLO-SINGING/blob/master/generate_rhysamples/Chinese/bad_Chinese.py "bad_Chinese.py") 

[rhy_model](https://github.com/AME430/TOWARDS-REFERENCE-INDEPENDENT-RHYTHM-ASSESSMENT-OF-SOLO-SINGING/tree/master/rhy_model "rhy_model") is the model we used to give evaluation score. At first we prepare the audios and rhythm histogram files, then use [createdata_paper.py](https://github.com/AME430/TOWARDS-REFERENCE-INDEPENDENT-RHYTHM-ASSESSMENT-OF-SOLO-SINGING/blob/master/rhy_model/hybrid_CRNN/create_data/createdata_paper.py "createdata_paper.py") to dump all files into one file which will be loaded in training and testing precess. Then [train_cqt_ph.py](https://github.com/AME430/TOWARDS-REFERENCE-INDEPENDENT-RHYTHM-ASSESSMENT-OF-SOLO-SINGING/blob/master/rhy_model/hybrid_CRNN/train/train_cqt_ph.py "train_cqt_ph.py") is used for training the model and [test_cqt_ph.py](https://github.com/AME430/TOWARDS-REFERENCE-INDEPENDENT-RHYTHM-ASSESSMENT-OF-SOLO-SINGING/blob/master/rhy_model/hybrid_CRNN/test/test_cqt_ph.py "test_cqt_ph.py") for test the model.

# Requirement
dill  
numpy  
librosa  
torch  
sklearn  
scipy  
wave  

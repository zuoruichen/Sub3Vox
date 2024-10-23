from faster_whisper import WhisperModel
import torch
import os
import pathlib
import pickle


# os.environ['CUDA_VISIBLE_DEVICES']='1'
# device = "cuda:1" if torch.cuda.is_available() else "cpu"

#path = "/home4c/mwmak/corpus/voxceleb2/test/aac/id03862/4wj3nWWwSQ4/00016.wav"  # /home4c/mwmak/corpus/voxceleb2/test/aac/id03862/_KwHFES8rsA/00317.wav  /home4c/mwmak/corpus/voxceleb2/test/aac/id03862/ob12OR6U74I/00425.wav
path = r"/home/data1/voxceleb2/dev/aac"    # /home4c/mwmak/corpus/voxceleb2/test/aac
#txtpath = "/Users/illusionist/Desktop/code/tdsvcorpus/txtvoxceleb2/dev"
timepath = "/home/ruichen/code/tdsvcorpus/timevoxceleb2/dev"  # /home/ruichen/code/tdsvcorpus/timevoxceleb2/dev  /home4b/ruichen/code/tdsvcorpus/timevoxceleb2/test

model_size = "large-v3"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", device_index=2, compute_type="float16")     # no use to set language here, work in model.transcribe()


# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")

# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")


def mytrans(mymodel, filepath):
    timestamplist=[]
# segments, info = model.transcribe(path, beam_size=5)
    segments, info = mymodel.transcribe(filepath, beam_size=5, word_timestamps=True)      # useful language setting

# print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))   # 句级时间戳

    for segment in segments:
        for word in segment.words:
            print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))  # 字级时间戳
            timestamplist.append((word.start, word.end, word.word))
    return timestamplist



def save_variable(v, filename):
    isExists=os.path.exists(filename[:-9])
    if not isExists:
        os.makedirs(filename[:-9])
    f = open(filename, 'wb')
    pickle.dump(v, f)
    f.close()

files = os.listdir(path)  # 得到文件夹下的所有文件名称
for idx in files:  # 遍历文件夹 idx: speaker id
    id_sub = os.listdir("{}/{}".format(path, idx))      #id_sub: session id
    if not os.path.exists("{}/{}".format(timepath, idx)):
        os.mkdir("{}/{}".format(timepath, idx))

    for i in id_sub:        # i: session id
        wavlist = list(pathlib.Path("{}/{}/{}".format(path, idx, i)).glob('*.wav'))
        # # 如果要捎带提取文件名的话，可以
        # xml_path_list = list(pathlib.Path(xml_file_path).glob('*.xml'))
        # xml_file_list = [i.name for i in xml_path_list]
#        print(wavlist)
#        f = open("{}/{}/{}.txt".format(timepath, idx, i), 'w')  # 读取label.txt文件，没有则创建，‘a’表示再次写入时不覆盖之前的内容

        for audio_path in wavlist:      # audiopath: 0000x.wav in session id
            audio_str = str(audio_path)
            if not os.path.exists("{}/{}/{}/{}.txt".format(timepath, idx, i, audio_str[-9:-4])):
                stamp = mytrans(model, audio_str)
                save_variable(stamp, "{}/{}/{}/{}.txt".format(timepath, idx, i, audio_str[-9:-4]))

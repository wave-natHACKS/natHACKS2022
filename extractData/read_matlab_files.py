import os
import numpy as np
import h5py
import data_loading_helpers as dh
import json

task = "NR"

rootdir = "./"
"""
https://stackoverflow.com/a/49677241
this to serialize json

"""
class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

sentences = {}

for file in os.listdir(rootdir):
    if file.endswith(task+".mat"):
        print(file)

        file_name = rootdir + file
        subject = file_name.split("ts")[1].split("_")[0]

        # exclude YMH due to incomplete data because of dyslexia
        if subject != 'YMH':

            f = h5py.File(file_name)
            sentence_data = f['sentenceData']
            #print(sentence_data)
            rawData = sentence_data['rawData']
            contentData = sentence_data['content']
            omissionR = sentence_data['omissionRate']
            wordData = sentence_data['word']

            # number of sentences:
            # print(len(rawData))
            wordDICT = dict()  # stores "word": {alpha: [], beta: [], gamma:[]}

            for idx in range(len(rawData) - len(rawData) + 1):
                obj_reference_content = contentData[idx][0]
                sent = dh.load_matlab_string(f[obj_reference_content])

                # get omission rate
                obj_reference_omr = omissionR[idx][0]
                omr = np.array(f[obj_reference_omr])
                print(omr)

                # get word level data
                word_data = dh.extract_word_level_data(f, f[wordData[idx][0]])

                # number of tokens
                # print(len(word_data))
                count = 0
                for widx in range(len(word_data)):
                
                    # get first fixation duration (FFD)
                    #print(word_data[widx]['FFD'])

                    # get aggregated EEG alpha features
                    #print(word_data[widx]['ALPHA_EEG'], " is alpha eeg")

                    #print(word_data[widx]["content"])


                
                    
                    # dictionary of {alphaVal: [], betaVal: []}
                    waveDict = dict()
                    waveDict["ALPHA_EEG"] = word_data[widx]['ALPHA_EEG']
                    waveDict["BETA_EEG"] = word_data[widx]['BETA_EEG']
                    waveDict["GAMMA_EEG"] = word_data[widx]['GAMMA_EEG']
                    waveDict["THETA_EEG"] = word_data[widx]['THETA_EEG']


                    wordDICT[word_data[widx]["content"]] = waveDict
                    

                    
                    
                dumped = json.dumps(wordDICT, cls=NumpyEncoder)
                with open ("onePhrase.json", "w") as outfile:
                    json.dump(dumped, outfile)
                #print(wordDICT)
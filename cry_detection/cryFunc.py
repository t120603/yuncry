#-*- coding: utf-8 -*-

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from scipy.io import wavfile

import os
import numpy as np
import csv
import pickle
import random, struct
from Crypto.Cipher import AES

#WaveMax = 32767

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

def feature_extraction(filename, framlen=0.128, shift=0.016):
    # read wav file
    [Fs, x] = audioBasicIO.readAudioFile(filename);
    if Fs == -1:
        return -1, -1, -1;
    elif len(x) == 0:
        return -1, -1, -1;
    
    # feature extraction
    F = audioFeatureExtraction.stFeatureExtraction(x, Fs, framlen*Fs, shift*Fs);
    vector = []
    vector_set = []

    if F.size == 0:
        return -1, -1, -1;

    # transpose
    # [34, N] => [N, 34]
    for i in range(0, len(F[0])):
        for j in range(0, len(F)):
            vector.append(F[j][i])
        vector_set.append(vector)
        vector = []
    
    return x, Fs, np.asarray(vector_set)
    
def normalize(source, average, stdevp):
    return (source - average)/float(stdevp)
    #return (source)/float(average)
    #return source
    
def normalize_list(source, parafile=''):
    if parafile == '':
        average = np.mean(source, axis=0)
        stdvp = np.std(source, axis=0)
    else:
        normalize_parameter = load_csv(parafile)
        average = normalize_parameter[0]
        stdvp = normalize_parameter[1]
    ret = []
    for vector in source:
        val_list = []
        for i in range(len(vector)):
            val_list.append( normalize(vector[i], average[i], stdvp[i]) )
        ret.append(val_list)
    return ret

def load_csv(csvfile):
    return np.loadtxt(open(csvfile,"rb"),delimiter=",",skiprows=0)
    
def cryDetection(filename):
    #Set
    framelen = 0.128
    shift = 0.064
    svm_model = pickle.load(open('OXmodel', 'rb'))
    
    x, Fs, fv_set = feature_extraction(filename, framelen, shift)
    if Fs == -1:
        print "File Error"
        print filename
        return
    fv_set = normalize_list(fv_set, 'nor_para2.csv')
    result = svm_model.predict(fv_set)
    cry_o = 0
    cry_x = 0
    for i in result:
        if i == 1:
            cry_o += 1
        else:
            cry_x += 1
    score = cry_o / float(cry_o+cry_x)
    if score > 0.2:
        return 1
    else:
        return 0
        
def cryDetection_special(filename):
    # Set
    framelen = 0.128
    shift = 0.064
    
    # Load model
    if os.path.exists('model'):
        decrypt_file('0jkdb52j5b2a34h8161y0dagf56n1fh6', 'model', 'OXmodel')
    else:
        print('[ERROR] not found \'model\'\n')
        return -1
    svm_model = pickle.load(open('OXmodel', 'rb'))
    os.remove('OXmodel')
    
    # feature extraction
    x, Fs, fv_set = feature_extraction(filename, framelen, shift)
    if Fs == -1:
        print "File Error"
        print filename
        return
        
    # normalize
    if os.path.exists('nor_para'):
        decrypt_file('0jkdb52j5b2a34h8161y0dagf56n1fh6', 'nor_para', 'nor_para2.csv')
    else:
        print('[ERROR] not found \'nor_para\'\n')
        return -1
    fv_set = normalize_list(fv_set, 'nor_para2.csv')
    os.remove('nor_para2.csv')
    
    # predict
    result = svm_model.predict(fv_set)
    cry_o = 0
    cry_x = 0
    for i in result:
        if i == 1:
            cry_o += 1
        else:
            cry_x += 1
    score = cry_o / float(cry_o+cry_x)
    
    # if the ratio of cry frame more than 0.2, and the audio is cry
    if score > 0.2:
        return 1
    else:
        return 0
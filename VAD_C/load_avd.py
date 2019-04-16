from ctypes import cdll
lib = cdll.LoadLibrary('lib_avd.so')

def VAD(filename):
    return lib.VAD(filename)

filename = "out.wav"

print(VAD(filename))

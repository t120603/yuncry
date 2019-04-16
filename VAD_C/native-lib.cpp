#include <jni.h>
#include <string>

extern "C" {
    #include "vad_main.h"
}

extern "C"
JNIEXPORT jint JNICALL
Java_com_dev_lungyu_lib_VoiceActivityDection_hasVoice(JNIEnv *env, jobject instance,
                                                      jstring folderpath_,
                                                      jstring filepath_) {
    const char *filepath = env->GetStringUTFChars(filepath_, 0);
    const char *folderpath = env->GetStringUTFChars(folderpath_, 0);

    // TODO
    int res = voivce_dection(folderpath,filepath);
    env->ReleaseStringUTFChars(filepath_, filepath);

    return res;
}



extern "C"
JNIEXPORT jstring JNICALL
Java_com_dev_lungyu_lib_VoiceActivityDection_stringFromJNI(JNIEnv *env, jobject instance) {

    // TODO
    std::string hello = "Hello from VAD C++";
    return env->NewStringUTF(hello.c_str());
}



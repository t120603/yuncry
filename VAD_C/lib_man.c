#include <stdlib.h> 
#include <stdio.h>
#include "vad_main.h"

int VAD(char* filepath){
    return voivce_dection("freqlevel.txt", filepath);
};


//extern "C" {
//  int VAD(char* freq_file,char* filepath){
//        return voivce_dection(freq_file, filepath);
//    };
//    int VAD(char* filepath){
//        return voivce_dection("freqlevel.txt", filepath);
//    };
//}

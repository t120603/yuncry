
#include <stdlib.h>
#include <stdio.h>
#include "vad_main.h"


int main(int argc,char** argv){
    char folderpath[] = "freqlevel.txt";
    char filepath[] = "1802242040.wav";
    
    printf("start... %s\n",argv[1]);    
    voivce_dection(folderpath,argv[1]);
    printf("end...");
    
    return 0;
}

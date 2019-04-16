//
// Created by lungyu on 9/18/17.
//

#include "vad_main.h"

int voivce_dection(const char *freqfile,const char *filepath) {
//    struct tm deadlinetm = {0, 0, 0, 1, 6 - 1, 2050 - 1900};
//    time_t deadlinetime = mktime(&deadlinetm);
//    time_t t = time(NULL);
//    if (t > deadlinetime) {
//        printf("[ERROR] Expired!\n");
//        return -2;
//    }

    if (filepath == NULL) {
        printf("[ERROR] path null!\n");
        return -1;
    }

//		struct tm *date = gmtime((time_t*)&t);
//		printf("%dŠ~ %d€ë %d€é", date->tm_year+1900, date->tm_mon+1, date->tm_mday);


    int i, frame = 0, temp, vad, num = 1000000000, count = 0, level[12];
    float n;
    float indata[FRAME_LEN], sum, avg = 0;
    //unsigned ;
    VadVars *vadstate;
    FILE *fp1, *f_out1, *read, *log;


    fp1 = fopen(filepath, "rb");

    if (!fp1) {
        printf("[ERROR] path error!\n");
        exit(-2);
    }


    f_out1 = fopen(freqfile, "w+");
    //log = fopen("outlog.txt", "a");
    wb_vad_init(&(vadstate));
    while (!feof(fp1)) {
        frame++;
        for (i = 0; i < FRAME_LEN; i++) {
            indata[i] = 0;
            temp = 0;
            fread(&temp, 2, 1, fp1);
            indata[i] = (float) temp;
            if (indata[i] > 65535 / 2)
                indata[i] = indata[i] - 65536;
        }
        vad = wb_vad(vadstate, indata);
        for (i = 0; i < 12; i++) {
            level[i] = 0;
        }

        fprintf(f_out1, "%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n", (vadstate->level[0]),
                ((vadstate->level[1])), (vadstate->level[2]), ((vadstate->level[3])),
                ((vadstate->level[4])), ((vadstate->level[5])), ((vadstate->level[6])),
                ((vadstate->level[7])), ((vadstate->level[8])), ((vadstate->level[9])),
                ((vadstate->level[10])), vadstate->level[11]);

    }

    fclose(fp1);
    fclose(f_out1);
    read = fopen(freqfile, "r");

    i = 0;
    count = 0;
    avg = 0;
    while (!feof(read)) {

        fscanf(read, "%f", &n);
        level[count] = n;
        if (count == 11) {
            sum = ((float) level[0] * 2 + (float) level[1] * 4 + (float) level[2] * 6 +
                   (float) level[3] * 8 + (float) level[4] * 12 + (float) level[5] * 16 +
                   (float) level[6] * 20 + (float) level[7] * 24 + (float) level[8] * 32 +
                   (float) level[9] * 40 + (float) level[10] * 48 + (float) level[11] * 64) /
                  10000000;

                //0.000011
            avg = avg + sum;
            count = 0;
            i++;
        } else {
            count++;
        }

    }
    fclose(read);
    float ret = avg / i;
    //printf("avg = %lf\n",avg);
    //printf("i = %d\n",i);
    printf("score = %lf\n",ret);
    //if ((avg / i) > 3.13 && (avg / i) < 3.27) {
    if ( ret > 0.1 && ret < 0.8) {
        printf("[Result] It is baby cry\n");
        return 1;
    } else {
        printf("[Result] non baby cry\n");
        return 0;
    }

    //fprintf(log,"%s: %f\n",filepath,(float)avg/i);
    return ret;

}

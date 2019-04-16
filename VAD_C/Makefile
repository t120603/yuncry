COMPILER = gcc -Wall -fPIC

LIB_OBJS = lib_man.o vad_main.o wb_vad.o
RUN_OBJS = wb_vad.o vad_main.o lib_man.o

run: wb_vad.o vad_main.o lib_man.o
    $(COMPILER) wb_vad.o vad_main.o lib_man.o run.c -o run -lm

lib: wb_vad.o vad_main.o lib_man.o
    $(COMPILER) -shared -o lib_vad.so $(LIB_OBJS)

run.o: run.c
    @echo Compiling run
    $(COMPILER) -c run.c -o run.o


wb_vad.o: wb_vad.c
    @echo Compiling wb_vad
    $(COMPILER) -c wb_vad.c -o wb_vad.o

vad_main.o: vad_main.c
    @echo Compiling vad_main.o
    $(COMPILER) -c vad_main.c -o vad_main.o

lib_man.o:lib_man.c
    @echo Compiling lib_man.o
    $(COMPILER) -c -fPIC lib_man.c -o lib_man.o

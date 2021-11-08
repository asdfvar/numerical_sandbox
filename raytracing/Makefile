CC = g++
MPI_CPP = $(HOME)/local/openmpi/v4.1.1/bin/mpic++

LIB_DIR = -L../gpnc/comm/ -L/home/euler/user_libs/libpng_1p6p37/lib/
LIB = -lcomm -lpng
INC = -I../gpnc/comm/ -I/home/euler/user_libs/libpng_1p6p37/include/

HEAD_OBJS = head.o write.o
BODY_OBJS = body.o object.o

all: LIBRARIES HEAD BODY

LIBRARIES:
	cd ../gpnc/comm/ && $(MAKE) -f comm.mk

head_exe = head.exe
body_exe = body.exe

HEAD: $(HEAD_OBJS)
	$(MPI_CPP) $^ $(LIB_DIR) $(LIB) -o $(head_exe)

BODY: $(BODY_OBJS)
	$(MPI_CPP) $^ $(LIB_DIR) $(LIB) -o $(body_exe)

clean:
	cd ../gpnc/comm/ && $(MAKE) -f comm.mk clean
	rm -f $(HEAD_OBJS) $(BODY_OBJS) $(head_exe) $(body_exe)

%.o: %.cpp
	$(MPI_CPP) $(INC) -c $^

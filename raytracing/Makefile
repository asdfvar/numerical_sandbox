CC = g++
MPI_CPP = $(HOME)/local/openmpi/v4.1.1/bin/mpic++

LIB_DIR = -L../gpnc/comm/
LIB = -lcomm
INC = -I../gpnc/comm/

BODY_OBJS = body.o object.o

all: LIBRARIES HEAD BODY

LIBRARIES:
	cd ../gpnc/comm/ && $(MAKE) -f comm.mk

HEAD: head.o
	$(MPI_CPP) $^ $(LIB_DIR) $(LIB) -o head.exe

BODY: $(BODY_OBJS)
	$(MPI_CPP) $^ $(LIB_DIR) $(LIB) -o body.exe

clean:
	cd ../gpnc/comm/ && $(MAKE) -f comm.mk clean
	rm head.o $(BODY_OBJS) head.exe body.exe

%.o: %.cpp
	$(MPI_CPP) $(INC) -c $^

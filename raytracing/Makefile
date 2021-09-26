CC = g++
MPI_CPP = $(HOME)/local/openmpi/v4.1.1/bin/mpic++

LIB_DIR = -L../gpnc/comm/
LIB = -lcomm
INC = -I../gpnc/comm/

all: LIBRARIES HEAD BODY

LIBRARIES:
	cd ../gpnc/comm/ && $(MAKE) -f comm.mk

HEAD: head.o
	$(MPI_CPP) $^ $(LIB_DIR) $(LIB) -o head.exe

BODY: body.o
	$(MPI_CPP) $^ $(LIB_DIR) $(LIB) -o body.exe

clean:
	cd ../gpnc/comm/ && $(MAKE) -f comm.mk clean
	rm head.o body.o head.exe body.exe

%.o: %.cpp
	$(MPI_CPP) $(INC) -c $^

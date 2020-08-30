#include "comm.h"

int main (int argc, char *argv[])
{
   const int num_stages = 3;

   comm::COMM Comm (&argc, &argv, num_stages, 1);

   return 0;
}

#include "comm.h"
#include "iostream"
#include "vector.h"
#include "object.h"

int main (int argc, char *argv[])
{
   std::cout << std::endl;

   const int num_stages = 2;

   comm::COMM Comm (&argc, &argv, num_stages, 0);

   std::cout << "test" << std::endl;

   const int array_size = 4;

   for (int rank = 0; rank < array_size; rank++) {
      Comm.send_to_stage (&rank, sizeof (rank), 1, rank, 0);
   }

   return 0;
}

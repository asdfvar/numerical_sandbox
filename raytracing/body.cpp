#include "comm.h"
#include "vector.h"
#include "object.h"
#include "iostream"

int main (int argc, char *argv[])
{
   const int num_stages = 2;

   const int tiles[2] = {4, 1};

   comm::COMM2D Comm (&argc, &argv, num_stages, 1, tiles);

   int value;
   Comm.receive_from_stage (&value, sizeof (value), 0, 0, 0);
   Comm.wait_for_receive_from_stage (0, 0, 0);

   std::cout << "rank = " << value << std::endl;

   return 0;
}

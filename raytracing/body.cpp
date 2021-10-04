#include "comm.h"
#include "vector.h"
#include "object.h"
#include "iostream"

int main (int argc, char *argv[])
{
   const int num_stages = 2;
   const int head_stage = 0;

   const int tiles[2] = {4, 1};

   comm::COMM2D Comm (&argc, &argv, num_stages, 1, tiles);

   int num_cell_rows;
   int num_cell_cols;
   int row_offset;
   float focal_length;

   Comm.receive_from_stage<float> (&focal_length,  sizeof (focal_length),  head_stage, 0, 0);
   Comm.receive_from_stage<int>   (&num_cell_rows, sizeof (num_cell_rows), head_stage, 0, 1);
   Comm.receive_from_stage<int>   (&num_cell_cols, sizeof (num_cell_cols), head_stage, 0, 2);
   Comm.receive_from_stage<int>   (&row_offset,    sizeof (row_offset),    head_stage, 0, 3);
   Comm.wait_for_receive_from_stage (head_stage, 0, 0);
   Comm.wait_for_receive_from_stage (head_stage, 0, 1);
   Comm.wait_for_receive_from_stage (head_stage, 0, 2);
   Comm.wait_for_receive_from_stage (head_stage, 0, 3);

   float *FPA = new float [num_cell_rows * num_cell_cols];

   delete[] FPA;

   return 0;
}

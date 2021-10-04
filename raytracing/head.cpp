#include "comm.h"
#include "iostream"
#include "vector.h"
#include "object.h"

#define NUM_CELL_ROWS 1000
#define NUM_CELL_COLS 1000
#define FOCAL_LENGTH  1.0f

int main (int argc, char *argv[])
{
   std::cout << std::endl;

   const int num_stages = 2;

   comm::COMM Comm (&argc, &argv, num_stages, 0);

   const int num_components = 4;

   // Define the focal plane array (FPA)
   float *FPA = new float [NUM_CELL_ROWS * NUM_CELL_COLS];

   {
      int q = NUM_CELL_ROWS / num_components;
      int r = NUM_CELL_ROWS % num_components;
      int row_offset = 0;

      float focal_length = FOCAL_LENGTH;

      // Divide the focal plane array into its components
      for (int rank = 0; rank < num_components; rank++) {
         int num_cell_cols = NUM_CELL_COLS;
         int num_cell_rows = q;
         if (rank < r) num_cell_rows += 1;

         Comm.send_to_stage<float> (&focal_length,  sizeof (focal_length),  1, rank, 0);
         Comm.send_to_stage<int>   (&num_cell_rows, sizeof (num_cell_rows), 1, rank, 1);
         Comm.send_to_stage<int>   (&num_cell_cols, sizeof (num_cell_cols), 1, rank, 2);
         Comm.send_to_stage<int>   (&row_offset,    sizeof (row_offset),    1, rank, 3);
         row_offset += num_cell_rows;
      }
   }

   delete[] FPA;

   return 0;
}

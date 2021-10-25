#include "comm.h"
#include "vector.h"
#include "object.h"
#include "iostream"
#include "ray.h"
#include "queue.h"

int main (int argc, char *argv[])
{
   const int num_stages = 2;
   const int head_stage = 0;
   const int head_rank  = 0;

   const int tiles[2] = {4, 1};

   comm::COMM2D Comm (&argc, &argv, num_stages, 1, tiles);

   int   num_cell_rows;
   int   num_cell_cols;
   int   row_offset;
   float focal_length;
   float window_width;
   float window_height;

   Comm.receive_from_stage<float> (&focal_length,  sizeof (focal_length),  head_stage, head_rank, 0);
   Comm.receive_from_stage<float> (&window_width,  sizeof (window_width),  head_stage, head_rank, 1);
   Comm.receive_from_stage<float> (&window_height, sizeof (window_height), head_stage, head_rank, 2);
   Comm.receive_from_stage<int>   (&num_cell_rows, sizeof (num_cell_rows), head_stage, head_rank, 3);
   Comm.receive_from_stage<int>   (&num_cell_cols, sizeof (num_cell_cols), head_stage, head_rank, 4);
   Comm.receive_from_stage<int>   (&row_offset,    sizeof (row_offset),    head_stage, head_rank, 5);

   Comm.wait_for_receive_from_stage (head_stage, head_rank, 0);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, 1);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, 2);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, 3);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, 4);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, 5);

   const float cell_width  = window_width  / static_cast<float> (num_cell_cols);
   const float cell_height = window_height / static_cast<float> (num_cell_rows);

   // Receive all the objects
   pQueue<Ball> ballQueue;

   int num_balls;
   Comm.receive_from_stage<int> (&num_balls, sizeof (num_balls), head_stage, head_rank, 6);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, 6);

   for (int ball_ind = 0; ball_ind < num_balls; ball_ind++) {
      Ball *ball = new Ball ();
      Comm.receive_from_stage<char> ((char*)ball, sizeof (Ball), head_stage, head_rank, 7);
      Comm.wait_for_receive_from_stage (head_stage, head_rank, 7);
      ballQueue.append (ball);
   }

   // test
   Ball *thing = ballQueue.pop ();
   thing->print_attr ();

   float *FPA = new float [num_cell_rows * num_cell_cols];

//    z   y
//    ^   ^
//    |  /
//    | /
//    |/
//    /
//    +----> x (look direction)

   for (int row_cell = row_offset, row_ind = 0; row_ind < num_cell_rows; row_cell++, row_ind++) {
      for (int col_cell = 0; col_cell < num_cell_cols; col_cell++) {

         // Determine the pointing vector as it passes through the center of the FPA cell
         float z_offset =  0.5f * window_height - cell_height * (0.5f - static_cast<float> (row_cell));
         float y_offset = -0.5f * window_width  + cell_width  * (0.5f + static_cast<float> (col_cell));
         float x_offset = focal_length;

         // Define the ray pointing out from the origin
         Ray ray;
         vec::Vector<float> position (0.0f, 0.0f, 0.0f);
         ray.position  = position;
         vec::Vector<float> pointing_vector (x_offset, y_offset, z_offset);
         pointing_vector.normalize ();
         ray.direction = pointing_vector;

         Queue<Ray> queue;
         queue.append (ray);
      }
   }

   delete[] FPA;

   return 0;
}

#include "comm.h"
#include "vector.h"
#include "object.h"
#include "iostream"
#include "ray.h"
#include "queue.h"
#include "tags.h"

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

   Comm.receive_from_stage<float> (&focal_length,  sizeof (focal_length),
         head_stage, head_rank, tag::focal_length);
   Comm.receive_from_stage<float> (&window_width,  sizeof (window_width), 
         head_stage, head_rank, tag::window_width);
   Comm.receive_from_stage<float> (&window_height, sizeof (window_height),
         head_stage, head_rank, tag::window_height);
   Comm.receive_from_stage<int>   (&num_cell_rows, sizeof (num_cell_rows),
         head_stage, head_rank, tag::num_cell_rows);
   Comm.receive_from_stage<int>   (&num_cell_cols, sizeof (num_cell_cols),
         head_stage, head_rank, tag::num_cell_cols);
   Comm.receive_from_stage<int>   (&row_offset,    sizeof (row_offset),
         head_stage, head_rank, tag::row_offset);

   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::focal_length);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::window_width);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::window_height);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::num_cell_rows);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::num_cell_cols);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::row_offset);

   const float cell_width  = window_width  / static_cast<float> (num_cell_cols);
   const float cell_height = window_height / static_cast<float> (num_cell_rows);

   // Receive all the objects

   // Receive all the balls from the head process
   pQueue<Ball> ballQueue;

   int num_balls;
   Comm.receive_from_stage<int> (&num_balls, sizeof (num_balls), head_stage, head_rank, tag::num_balls);
   Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::num_balls);

   for (int ball_ind = 0; ball_ind < num_balls; ball_ind++) {
      Ball *ball = new Ball ();
      Comm.receive_from_stage ((char*)ball, sizeof (*ball), head_stage, head_rank, tag::ball);
      Comm.wait_for_receive_from_stage (head_stage, head_rank, tag::ball);
      ballQueue.append (ball);
   }

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

         // Define the ray pointing out from the origin (0,0,0) pointing through the FPA cell
         Ray ray;
         vec::Vector<float> position (0.0f, 0.0f, 0.0f);
         ray.position  = position;
         vec::Vector<float> pointing_vector (x_offset, y_offset, z_offset);
         pointing_vector.normalize ();
         ray.direction = pointing_vector;

         // Append the ray to the queue of rays
         Queue<Ray> queue;
         queue.append (ray);

         // Process the queue of rays until it becomes empty
         while (queue.num_el () > 0) {
            ray = queue.pop ();

            pQueue<Ball> holder;
            while (ballQueue.num_el () > 0) {
               Ball *ball = ballQueue.pop ();
               holder.append (ball);

               if (ball->intersect (ray.position, ray.direction)) {
                  // logic to determine new ray direction and another ray pointing towards each
                  // light source
               }
            }

            // Move the balls back into the original ball queue
            while (holder.num_el () > 0) ballQueue.append (holder.pop ());
         }

      }
   }

   delete[] FPA;

   return 0;
}

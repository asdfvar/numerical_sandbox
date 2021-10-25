#include "comm.h"
#include "iostream"
#include "vector.h"
#include "object.h"
#include "queue.h"

#define NUM_CELL_ROWS 1000
#define NUM_CELL_COLS 1000
#define FOCAL_LENGTH  1.0f
#define WINDOW_WIDTH  1.0f
#define WINDOW_HEIGHT 1.0f

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

      float focal_length  = FOCAL_LENGTH;
      float window_width  = WINDOW_WIDTH;
      float window_height = WINDOW_HEIGHT;

      // Divide the focal plane array into as equally-spaced as possible horizontal components
      for (int rank = 0; rank < num_components; rank++) {
         int num_cell_cols = NUM_CELL_COLS;
         int num_cell_rows = q;
         if (rank < r) num_cell_rows += 1;

         Comm.send_to_stage<float> (&focal_length,  sizeof (focal_length),  1, rank, 0);
         Comm.wait_for_send_to_stage (1, rank, 0);
         Comm.send_to_stage<float> (&window_width,  sizeof (window_width),  1, rank, 1);
         Comm.wait_for_send_to_stage (1, rank, 1);
         Comm.send_to_stage<float> (&window_height, sizeof (window_height), 1, rank, 2);
         Comm.wait_for_send_to_stage (1, rank, 2);
         Comm.send_to_stage<int>   (&num_cell_rows, sizeof (num_cell_rows), 1, rank, 3);
         Comm.wait_for_send_to_stage (1, rank, 3);
         Comm.send_to_stage<int>   (&num_cell_cols, sizeof (num_cell_cols), 1, rank, 4);
         Comm.wait_for_send_to_stage (1, rank, 4);
         Comm.send_to_stage<int>   (&row_offset,    sizeof (row_offset),    1, rank, 5);
         Comm.wait_for_send_to_stage (1, rank, 5);
         row_offset += num_cell_rows;
      }
   }

   // Build the queue of balls
   pQueue<Ball> ballQueue;
   ballQueue.append (new Ball (vec::Vector<float> (10.0f, 0.0f, 0.0f), 4.0f));
// FIXME: appears that Comm can't send multiple messages to the same tag
//   ballQueue.append (new Ball (vec::Vector<float> (-10.0f, 0.0f, 0.0f), 7.0f));

   int num_balls = ballQueue.num_el ();
   for (int rank = 0; rank < num_components; rank++) {
      Comm.send_to_stage<int> (&num_balls, sizeof (num_balls), 1, rank, 6);
      Comm.wait_for_send_to_stage (1, rank, 6);
   }

#if 1
   for (int ball_ind = 0; ball_ind < num_balls; ball_ind++) {

      Ball *ball = static_cast<Ball*> (ballQueue.pop ());
      for (int rank = 0; rank < num_components; rank++) {
         char *ptr = (char*)ball;
         Comm.send_to_stage<char> (ptr, sizeof (Ball), 1, rank, 7);
         Comm.wait_for_send_to_stage (1, rank, 7);
      }
   }
#endif

   delete[] FPA;

   return 0;
}

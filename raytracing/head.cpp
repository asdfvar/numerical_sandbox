#include "comm.h"
#include "iostream"
#include "vector.h"
#include "object.h"
#include "queue.h"
#include "tags.h"

#define NUM_CELL_ROWS 1000
#define NUM_CELL_COLS 1000
#define FOCAL_LENGTH  1.0f
#define WINDOW_WIDTH  1.0f
#define WINDOW_HEIGHT 1.0f

int main (int argc, char *argv[])
{
   std::cout << std::endl;

   const int num_stages = 2;
   const int this_module = 0;

   comm::COMM Comm (&argc, &argv, stage::NUM_MODULES, this_module);

   const int num_components = 4;

   // Define the focal plane array (FPA)
   float *FPA = new float [NUM_CELL_ROWS * NUM_CELL_COLS];

   int q = NUM_CELL_ROWS / num_components;
   int r = NUM_CELL_ROWS % num_components;
   int row_offset = 0;

   float focal_length  = FOCAL_LENGTH;
   float window_width  = WINDOW_WIDTH;
   float window_height = WINDOW_HEIGHT;

   // Send attributes about the FPA to the body processes
   for (int rank = 0; rank < num_components; rank++)
   {
      // Divide the focal plane array into as equally-spaced as possible horizontal components
      int num_cell_cols = NUM_CELL_COLS;
      int num_cell_rows = q;
      if (rank < r) num_cell_rows += 1;

      Comm.send_to_stage<float> (
            &focal_length,
            1,
            stage::BODY_MODULE,
            rank,
            tag::focal_length);

      Comm.wait_for_send_to_stage (
            stage::BODY_MODULE,
            rank,
            tag::focal_length);

      Comm.send_to_stage<float> (
            &window_width,
            1,
            stage::BODY_MODULE,
            rank,
            tag::window_width);

      Comm.wait_for_send_to_stage (
            stage::BODY_MODULE,
            rank,
            tag::window_width);

      Comm.send_to_stage<float> (
            &window_height,
            1,
            stage::BODY_MODULE,
            rank,
            tag::window_height);

      Comm.wait_for_send_to_stage (
            stage::BODY_MODULE,
            rank,
            tag::window_height);

      Comm.send_to_stage<int> (
            &num_cell_rows,
            1,
            stage::BODY_MODULE,
            rank,
            tag::num_cell_rows);

      Comm.wait_for_send_to_stage (
            stage::BODY_MODULE,
            rank,
            tag::num_cell_rows);

      Comm.send_to_stage<int> (
            &num_cell_cols,
            1,
            stage::BODY_MODULE,
            rank,
            tag::num_cell_cols);

      Comm.wait_for_send_to_stage (
            stage::BODY_MODULE,
            rank,
            tag::num_cell_cols);

      Comm.send_to_stage<int> (
            &row_offset,
            1,
            stage::BODY_MODULE,
            rank,
            tag::row_offset);

      Comm.wait_for_send_to_stage (
            stage::BODY_MODULE,
            rank,
            tag::row_offset);

      row_offset += num_cell_rows;
   }

   // Build the queue of balls
   pQueue<Ball> ballQueue;
   ballQueue.append (new Ball (vec::Vector<float> (10.0f, 0.0f, 0.0f), 4.0f));
   ballQueue.append (new Ball (vec::Vector<float> (-10.0f, 0.0f, 0.0f), 7.0f));

   // Inform the body processes of the number of balls
   int num_balls = ballQueue.num_el ();
   for (int rank = 0; rank < num_components; rank++) {
      Comm.send_to_stage<int> (&num_balls, 1, stage::BODY_MODULE, rank, tag::num_balls);
      Comm.wait_for_send_to_stage (1, rank, tag::num_balls);
   }

   // Send the balls to the body processes
   for (int ball_ind = 0; ball_ind < num_balls; ball_ind++) {
      Ball *ball = static_cast<Ball*> (ballQueue.pop ());
      for (int rank = 0; rank < num_components; rank++) {
         Comm.send_to_stage ((char*)ball, sizeof (*ball), 1, rank, tag::ball);
         Comm.wait_for_send_to_stage (1, rank, tag::ball);
      }
   }

   // Build the queue of light sources
   Queue< vec::Vector<float> > lightQueue;
   lightQueue.append (vec::Vector<float> (10.0f, 0.0f, 10.0f));
   lightQueue.append (vec::Vector<float> (10.0f, 10.0f, 0.0f));

   // Inform the body processes of the number of light sources
   int num_lights = lightQueue.num_el ();
   for (int rank = 0; rank < num_components; rank++) {
      Comm.send_to_stage<int> (&num_lights, 1, stage::BODY_MODULE, rank, tag::num_lights);
      Comm.wait_for_send_to_stage (1, rank, tag::num_lights);
   }

   // Send the light sources to the body processes
   for (int light_ind = 0; light_ind < num_lights; light_ind++) {
      vec::Vector<float> light = lightQueue.pop ();
      for (int rank = 0; rank < num_components; rank++) {
         Comm.send_to_stage (
               (char*)&light, sizeof (light), stage::BODY_MODULE, rank, tag::light_source);
         Comm.wait_for_send_to_stage (1, rank, tag::light_source);
      }
   }

   delete[] FPA;

   return 0;
}

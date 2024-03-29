#include "comm.h"
#include "iostream"
#include "vector.h"
#include "object.h"
#include "queue.h"
#include "tags.h"
#include "write.h"

#define NUM_CELL_ROWS 1000
#define NUM_CELL_COLS 1000
#define FOCAL_LENGTH  1.0f
#define WINDOW_WIDTH  1.0f
#define WINDOW_HEIGHT 1.0f

int main (int argc, char *argv[])
{
   std::cout << std::endl;

   const int this_module = 0;

   comm::COMM Comm (&argc, &argv, stage::NUM_MODULES, this_module);

   const int num_components = 7;

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

      Comm.send_to_stage<float> (&focal_length, 1, stage::BODY_MODULE, rank, tag::focal_length);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::focal_length);

      Comm.send_to_stage<float> (&window_width, 1, stage::BODY_MODULE, rank, tag::window_width);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::window_width);

      Comm.send_to_stage<float> (&window_height, 1, stage::BODY_MODULE, rank, tag::window_height);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::window_height);

      Comm.send_to_stage<int> (&num_cell_rows, 1, stage::BODY_MODULE, rank, tag::num_cell_rows);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::num_cell_rows);

      Comm.send_to_stage<int> (&num_cell_cols, 1, stage::BODY_MODULE, rank, tag::num_cell_cols);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::num_cell_cols);

      Comm.send_to_stage<int> (&row_offset, 1, stage::BODY_MODULE, rank, tag::row_offset);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::row_offset);

      row_offset += num_cell_rows;
   }

   // Build the queue of balls
   pQueue<Ball> ballQueue;
//   ballQueue.append (new Ball (vec::Vector<float> (10.0f, -1.0f, -0.5f), 4.0f));
   ballQueue.append (new Ball (vec::Vector<float> (9.7f,  1.0f, 0.0f), 4.0f));
//   ballQueue.append (new Ball (vec::Vector<float> (-10.0f, 0.0f, 0.0f), 7.0f));

   // Inform the body processes of the number of balls
   int num_balls = ballQueue.num_el ();
   for (int rank = 0; rank < num_components; rank++) {
      Comm.send_to_stage<int> (&num_balls, 1, stage::BODY_MODULE, rank, tag::num_balls);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::num_balls);
   }

   // Send the balls to the body processes
   for (int ball_ind = 0; ball_ind < num_balls; ball_ind++) {
      Ball *ball = static_cast<Ball*> (ballQueue.pop ());
      for (int rank = 0; rank < num_components; rank++) {
         Comm.send_to_stage ((char*)ball, sizeof (*ball), 1, rank, tag::ball);
         Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::ball);
      }
   }

   pQueue<Triangle> triangleQueue;

   // Build the queue of triangles
   vec::Vector<float> corners[3];
   corners[0].x = 5.0f; corners[0].y = -5.0f; corners[0].z =  0.0f;
   corners[1].x = 5.1f; corners[1].y =  5.0f; corners[1].z =  2.0f;
   corners[2].x = 4.9f; corners[2].y =  3.0f; corners[2].z = -1.0f;
   triangleQueue.append (new Triangle (corners));

   // Inform the body processes of the number of triangles
   int num_triangles = triangleQueue.num_el ();
   for (int rank = 0; rank < num_components; rank++) {
      Comm.send_to_stage<int> (&num_triangles, 1, stage::BODY_MODULE, rank, tag::num_triangles);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::num_triangles);
   }

   // Send the triangles to the body processes
   for (int triangle_ind = 0; triangle_ind < num_triangles; triangle_ind++) {
      Triangle *triangle = static_cast<Triangle*> (triangleQueue.pop ());
      for (int rank = 0; rank < num_components; rank++) {
         Comm.send_to_stage ((char*)triangle, sizeof (*triangle), 1, rank, tag::triangle);
         Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::triangle);
      }
   }

   // Build the queue of light sources
   Queue< vec::Vector<float> > lightQueue;
   lightQueue.append (vec::Vector<float> (3.0f, -10.0f, 10.0f));
//   lightQueue.append (vec::Vector<float> (-10.0f, 0.0f, 0.0f));
//   lightQueue.append (vec::Vector<float> (10.0f, 10.0f, 0.0f));

   // Inform the body processes of the number of light sources
   int num_lights = lightQueue.num_el ();
   for (int rank = 0; rank < num_components; rank++) {
      Comm.send_to_stage<int> (&num_lights, 1, stage::BODY_MODULE, rank, tag::num_lights);
      Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::num_lights);
   }

   // Send the light sources to the body processes
   for (int light_ind = 0; light_ind < num_lights; light_ind++) {
      vec::Vector<float> light = lightQueue.pop ();
      for (int rank = 0; rank < num_components; rank++) {
         Comm.send_to_stage (
               (char*)&light, sizeof (light), stage::BODY_MODULE, rank, tag::light_source);
         Comm.wait_for_send_to_stage (stage::BODY_MODULE, rank, tag::light_source);
      }
   }

   // Define the focal plane array (FPA)
   float *FPA[3];
   FPA[0] = new float [NUM_CELL_ROWS * NUM_CELL_COLS];
   FPA[1] = new float [NUM_CELL_ROWS * NUM_CELL_COLS];
   FPA[2] = new float [NUM_CELL_ROWS * NUM_CELL_COLS];

   for (int channel = 0; channel < 3; channel++) {
      float *pFPA = FPA[channel];

      // Receive the complete FPA from each of the body processes
      for (int rank = 0; rank < num_components; rank++)
      {
         // Divide the focal plane array into as equally-spaced as possible horizontal components
         int num_cell_cols = NUM_CELL_COLS;
         int num_cell_rows = q;
         if (rank < r) num_cell_rows += 1;

         // Receive the FPA chunk for this rank
         Comm.receive_from_stage<float> (pFPA, num_cell_rows * num_cell_cols, stage::BODY_MODULE, rank, tag::fpa);
         Comm.wait_for_receive_from_stage (stage::BODY_MODULE, rank, tag::fpa);

         pFPA += num_cell_cols * num_cell_rows;
      }
   }

   write_grayscale_png (FPA, NUM_CELL_COLS, NUM_CELL_ROWS, "image.png");

   delete[] FPA[0];
   delete[] FPA[1];
   delete[] FPA[2];

   return 0;
}

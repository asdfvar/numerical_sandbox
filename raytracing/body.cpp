#include "comm.h"
#include "vector.h"
#include "object.h"
#include "iostream"
#include "ray.h"
#include "queue.h"
#include "tags.h"
#include <cmath>

#define TOTAL_NUM_CELL_ROWS 1000
#define PI 3.14159265358979323

int main (int argc, char *argv[])
{
   const int head_rank  = 0;
   const int this_module = 1;

   const int tiles[2] = {4, 1};

   comm::COMM2D Comm (&argc, &argv, stage::NUM_MODULES, this_module, tiles);

   int   num_cell_rows;
   int   num_cell_cols;
   int   row_offset;
   float focal_length;
   float window_width;
   float window_height;

   Comm.receive_from_stage<float> (&focal_length,  sizeof (focal_length),
         stage::HEAD_MODULE, head_rank, tag::focal_length);
   Comm.receive_from_stage<float> (&window_width,  sizeof (window_width), 
         stage::HEAD_MODULE, head_rank, tag::window_width);
   Comm.receive_from_stage<float> (&window_height, sizeof (window_height),
         stage::HEAD_MODULE, head_rank, tag::window_height);
   Comm.receive_from_stage<int>   (&num_cell_rows, sizeof (num_cell_rows),
         stage::HEAD_MODULE, head_rank, tag::num_cell_rows);
   Comm.receive_from_stage<int>   (&num_cell_cols, sizeof (num_cell_cols),
         stage::HEAD_MODULE, head_rank, tag::num_cell_cols);
   Comm.receive_from_stage<int>   (&row_offset,    sizeof (row_offset),
         stage::HEAD_MODULE, head_rank, tag::row_offset);

   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::focal_length);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::window_width);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::window_height);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::num_cell_rows);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::num_cell_cols);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::row_offset);

   const float cell_width  = window_width  / static_cast<float> (num_cell_cols);
   const float cell_height = window_height / static_cast<float> (TOTAL_NUM_CELL_ROWS);

   /* Receive all the objects */

   // Receive all the balls from the head process
   pQueue<Ball> ballQueue;

   int num_balls;
   Comm.receive_from_stage<int> (&num_balls, 1, stage::HEAD_MODULE, head_rank, tag::num_balls);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::num_balls);

   for (int ball_ind = 0; ball_ind < num_balls; ball_ind++)
   {
      Ball *ball = new Ball ();

      Comm.receive_from_stage (
            (char*)ball,
            sizeof (*ball),
            stage::HEAD_MODULE,
            head_rank,
            tag::ball);

      Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::ball);
      ballQueue.append (ball);
   }

   // Receive all the triangles from the head process
   pQueue<Triangle> triangleQueue;

   int num_triangles;

   Comm.receive_from_stage<int> (&num_triangles,
         1,
         stage::HEAD_MODULE,
         head_rank,
         tag::num_triangles);

   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::num_triangles);

   for (int triangle_ind = 0; triangle_ind < num_triangles; triangle_ind++)
   {
      Triangle *triangle = new Triangle ();

      Comm.receive_from_stage (
            (char*)triangle,
            sizeof (*triangle),
            stage::HEAD_MODULE,
            head_rank,
            tag::triangle);

      Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::triangle);
      triangleQueue.append (triangle);
   }

   // Receive all the light sources from the head process
   Queue< vec::Vector<float> > lightQueue;

   int num_lights;
   Comm.receive_from_stage<int> (&num_lights, 1, stage::HEAD_MODULE, head_rank, tag::num_lights);
   Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::num_lights);

   for (int light_ind = 0; light_ind < num_lights; light_ind++)
   {
      vec::Vector<float> light;

      Comm.receive_from_stage (
            (char*)&light,
            sizeof (light),
            stage::HEAD_MODULE,
            head_rank,
            tag::light_source);

      Comm.wait_for_receive_from_stage (stage::HEAD_MODULE, head_rank, tag::light_source);
      lightQueue.append (light);
   }

   float *FPA[3];
   FPA[0] = new float [num_cell_rows * num_cell_cols];
   FPA[1] = new float [num_cell_rows * num_cell_cols];
   FPA[2] = new float [num_cell_rows * num_cell_cols];

//    z   y
//    ^   ^
//    |  /
//    | /
//    |/
//    /
//    +----> x (look direction)

   // Loop through each FPA cell this process is responsible for
   for (int row_cell = row_offset, row_ind = 0, cell_ind = 0;
         row_ind < num_cell_rows;
         row_cell++, row_ind++)
   {
      for (int col_cell = 0; col_cell < num_cell_cols; col_cell++, cell_ind++)
      {
         FPA[0][cell_ind] = 0.0f;
         FPA[1][cell_ind] = 0.0f;
         FPA[2][cell_ind] = 0.0f;

         // Determine the pointing vector as it passes through the center of the FPA cell
         float z_offset =  0.5f * window_height -
            cell_height * (0.5f + static_cast<float> (row_cell));
         float y_offset = -0.5f * window_width  +
            cell_width  * (0.5f + static_cast<float> (col_cell));
         float x_offset = focal_length;

         // Define the ray pointing out from the origin (0,0,0) and through the FPA cell
         Ray<float> ray;
         vec::Vector<float> position (0.0f, 0.0f, 0.0f);
         ray.position  = position;
         vec::Vector<float> pointing_vector (x_offset, y_offset, z_offset);
         pointing_vector.normalize ();
         ray.direction = pointing_vector;

         // Append the ray to the queue of rays
         Queue< Ray<float> > ray_queue;
         ray_queue.append (ray);

         // Process the queue of rays until it becomes empty
         while (ray_queue.num_el () > 0) {
            ray = ray_queue.pop ();

            // Instantiate a new container to hold the balls popped off the ball queue
            pQueue<Ball> holder;

            bool  intersect_ray    = false;
            float min_distance     = 0.0f;
            int   nearest_obj_ind = 0;

            // Find which ball intersects this ray
            for (int ball_ind = 0; ball_ind < ballQueue.num_el (); ball_ind++)
            {
               Ball *ball = ballQueue.access (ball_ind);

               if (ball->intersect (ray)) {
                  float distance = ball->distance (ray);
                  if (intersect_ray == false || distance < min_distance) {
                     min_distance = distance;
                     nearest_obj_ind = ball_ind;
                  }

                  intersect_ray = true;
               }
            }

            if (intersect_ray)
            {
               Ball *ball = ballQueue.access (nearest_obj_ind);

               // Get the reflected ray
               Ray<float> reflected_ray = ball->reflect (ray);

               // Loop through each light source
               for (int light_ind = 0; light_ind < lightQueue.num_el (); light_ind++)
               {
                  vec::Vector <float> light_source = lightQueue.access (light_ind);

                  // Get the ray pointing toward this light source
                  Ray<float> ray_toward_light_source = reflected_ray;
                  ray_toward_light_source.direction = light_source - reflected_ray.position;
                  ray_toward_light_source.direction.normalize ();

                  // Find the angle between the reflected ray and the ray toward the light source.
                  // Using u * v = |u|*|v|*cos (theta) and it's assumed |u| = |v| = 1
                  float udv = ray_toward_light_source.direction * reflected_ray.direction;

                  if (udv < 0.0f) udv = 0.0f;
                  vec::Vector<float> color = ball->reflected_color (udv);

                  FPA[0][cell_ind] += color.x;
                  FPA[1][cell_ind] += color.y;
                  FPA[2][cell_ind] += color.z;
               }
            }
         }
      }
   }

   // Send the result back to the head process
   for (int channel = 0; channel < 3; channel++) {
      Comm.send_to_stage (
            FPA[channel],
            num_cell_rows * num_cell_cols,
            stage::HEAD_MODULE,
            head_rank,
            tag::fpa);

      Comm.wait_for_send_to_stage (stage::HEAD_MODULE, head_rank, tag::fpa);
   }

   delete[] FPA[0];
   delete[] FPA[1];
   delete[] FPA[2];

   return 0;
}

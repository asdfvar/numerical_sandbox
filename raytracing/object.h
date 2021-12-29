#ifndef OBJECT_H
#define OBJECT_H

#include "ray.h"
#include <iostream>

static const int color_array_len = 21;

template <typename type> class Object {
   public:
      Object (void) {
         color.x = 1.0f;
         color.y = 1.0f;
         color.z = 1.0f;
      };

      void set_color (vec::Vector<type> color);
      vec::Vector<type> reflected_color (type gradient);

   private:
      vec::Vector<type> color;
};

class Ball : public Object<float> {
   public:
      Ball (void) : Object<float> () { };

      Ball (vec::Vector<float> center_in, float radius_in) : Object<float> () {
         center = center_in;
         radius = radius_in;
      }

      bool  intersect (Ray<float> ray);
      float distance  (Ray<float> ray);

      Ray<float> reflect (Ray<float> ray);

      void print (void) {
         std::cout << "radius = " << radius << std::endl;
         std::cout << "center = " << center.x << ", " << center.y << ", " <<
            center.z << std::endl;
      }

   private:
      vec::Vector<float> center;
      float radius;
};

class Triangle : public Object<float> {
   public:
      Triangle (void) : Object<float> () { };

      Triangle (vec::Vector<float> corners_in[3]) : Object<float> () {
         corners[0] = corners_in[0];
         corners[1] = corners_in[1];
         corners[2] = corners_in[2];

         vec::Vector<float> a = corners[1] - corners[0];
         vec::Vector<float> b = corners[2] - corners[0];

         // Normal of this plane
         normal = b.cross (a);
         normal.normalize ();

         // Equation of this plane
         RHS = normal * a;
      }

      bool  intersect (Ray<float> ray);
      float distance  (Ray<float> ray);

      Ray<float> reflect (Ray<float> ray);

   private:
      vec::Vector<float> corners[3];
      vec::Vector<float> normal;
      float RHS;
};

#endif

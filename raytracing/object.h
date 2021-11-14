#ifndef OBJECT_H
#define OBJECT_H

#include "ray.h"
#include <iostream>

template <typename type> class Object {
   public:
//      virtual bool intersect (vec::Vector<type> Position, vec::Vector<type> Direction) = 0;
//      virtual void print_attr (void) { std::cout << "base class" << std::endl; }
};

class Ball : public Object<float> {
   public:
      Ball (void) { };

      Ball (vec::Vector<float> center_in, float radius_in) {
         center = center_in;
         radius = radius_in;
      }

      bool  intersect (Ray<float> ray);
      float distance  (Ray<float> ray);

      Ray<float> reflect (Ray<float> ray);

      void print (void) {
         std::cout << "radius = " << radius << std::endl;
         std::cout << "center = " << center.x << ", " << center.y << ", " << center.z << std::endl;
      }

   private:
      vec::Vector<float> center;
      float radius;
};

#endif

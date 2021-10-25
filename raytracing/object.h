#ifndef OBJECT_H
#define OBJECT_H

#include "vector.h"
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

      // Determine if the vector starting at "position" and pointing in "direction" intersect
      // the ball by comparing the length from the relation
      // length^2 + ((center - position) * direction)^2 = |center - position|^2
      // with the radius of the ball. The length is the closest distance from the center of the
      // ball to the line projected by the vector.
      bool intersect (vec::Vector<float> position, vec::Vector<float> direction) {
         direction.normalize ();
         vec::Vector<float> pmx = center - position;
         float length2 = vec::norm2<float> (pmx) / ((pmx * direction) * (pmx * direction));
         float length;
         if (length2 > 0.000001f) {
            length = sqrt (length2);
         } else {
            length = 0.0f;
         }
         return length <= radius;
      }

      void print_attr (void) {
         std::cout << "radius = " << radius << std::endl;
      }

   private:
      vec::Vector<float> center;
      float radius;
};

#endif

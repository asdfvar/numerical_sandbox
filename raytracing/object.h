#ifndef OBJECT_H
#define OBJECT_H
#include "vector.h"

template <typename type> class Object {

   public:
      virtual bool intersect (Vector<type> Position, Vector<type> Direction) = 0;
};

template <typename type> class Ball : public Object<type> {
   public:
      Ball (Vector<type> center_in, float radius_in) {
         center = center_in;
         radius = radius_in;
      }

      bool intersect (Vector<type> Position, Vector<type> Direction) {
         return true;
      }

   private:
      Vector<type> center;
      float radius;
};

#endif

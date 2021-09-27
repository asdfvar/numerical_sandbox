#ifndef OBJECT_H
#define OBJECT_H
#include "vector.h"

template <typename type> class Object {

   public:
      virtual bool intersect (Vector<type> Position, Vector<type> Direction) = 0;
};

template <typename type> class Ball : public Object<type> {
   public:
      Ball (Vector<type> center_in, float radius) {
         center = center_in;
      }

      bool intersect (Vector<type> v) {
         return true;
      }

   private:
      Vector<type> center;
};

#endif
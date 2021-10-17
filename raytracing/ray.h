#ifndef RAY_H
#define RAY_H

#include "vector.h"

class Ray {
   public:
      vec::Vector<float> position;
      vec::Vector<float> direction;
};

#endif

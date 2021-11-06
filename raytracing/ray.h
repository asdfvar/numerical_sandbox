#ifndef RAY_H
#define RAY_H

#include "vector.h"

template <typename type> class Ray {
   public:
      vec::Vector<type> position;
      vec::Vector<type> direction;

      type intensity[3];
};

#endif

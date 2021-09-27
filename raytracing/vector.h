#ifndef VECTOR_H
#define VECTOR_H

template <typename type> class Vector {
   public:
      Vector (type x_in, type y_in, type z_in) {
         x = x_in;
         y = y_in;
         z = z_in;
      }

      Vector operator+(const Vector& vector) const {
         Vector result (x + vector.x, y + vector.y, z + vector.z);
         return result;
      }

      type x, y, z;
};

#endif

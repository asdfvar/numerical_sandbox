#ifndef VECTOR_H
#define VECTOR_H

#include <cmath>

namespace vec {
   template <typename type> class Vector {
      public:
         Vector (void) {
            x = 0;
            y = 0;
            z = 0;
         }

         Vector (type x_in, type y_in, type z_in) {
            x = x_in;
            y = y_in;
            z = z_in;
         }

         Vector operator+(const Vector& vector) const {
            Vector result (x + vector.x, y + vector.y, z + vector.z);
            return result;
         }

         Vector operator-(const Vector& vector) const {
            Vector result (x - vector.x, y - vector.y, z - vector.z);
            return result;
         }

         type operator*(const Vector& vector) const {
            return vector.x * x + vector.y * y + vector.z * z;
         }

         Vector operator*(const float number) const {
            Vector new_vector;
            new_vector.x = x * number;
            new_vector.y = y * number;
            new_vector.z = z * number;
            return new_vector;
         }

         void normalize (void)
         {
            type mag = static_cast<type> (sqrt (x * x + y * y + z * z));
            x /= mag;
            y /= mag;
            z /= mag;
         }

         type x, y, z;
   };

   template <typename type> type norm2 (const Vector<type> vector) {
      return vector.x * vector.x + vector.y * vector.y + vector.z * vector.z; 
   }

}

#endif

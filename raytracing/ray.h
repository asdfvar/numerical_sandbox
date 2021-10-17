#ifndef RAY_H
#define RAY_H

#include "vector.h"

class Ray {
   public:
      vec::Vector<float> position;
      vec::Vector<float> direction;
      float channels[3];
};

template <typename Type> class NODE {
   public:
      Type obj;
      NODE<Type> *next;
};

template <typename Type> class Queue {

   public:
      Queue (void) {
         front = back = NULL;
         queue_size = 0;
      }

      void append (Type obj) {
         if (queue_size == 0) front = back = new NODE<Type>;
         else {
            back->next = new NODE<Type>;
            back = back->next;
            back->obj = obj;
            queue_size++;
         }
      }

      Type pop (void) {
         Type obj;
         if (queue_size <= 0) return obj;

         obj = front->obj;
         NODE<Type> *old = front;
         front = front->next;
         delete old;
         queue_size--;
         return obj;
      }

      ~Queue (void) { while (queue_size > 0) pop (); }

   private:
      NODE<Type> *front, *back;
      int queue_size;
};

#endif

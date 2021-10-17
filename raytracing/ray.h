#ifndef RAY_H
#define RAY_H

#include "vector.h"

class Ray {
   public:
      vec::Vector<float> position;
      vec::Vector<float> direction;
      float channels[3];
};

class NODE {
   public:
      Ray ray;
      NODE *next;
};

class Queue {

   public:
      Queue (void) {
         front = back = NULL;
         queue_size = 0;
      }

      void append (Ray ray) {
         if (queue_size == 0) front = back = new NODE;
         else {
            back->next = new NODE;
            back = back->next;
            back->ray = ray;
            queue_size++;
         }
      }

      Ray pop (void) {
         Ray ray;
         if (queue_size <= 0) return ray;

         ray = front->ray;
         NODE *old = front;
         front = front->next;
         delete old;
         queue_size--;
         return ray;
      }

      ~Queue (void) { while (queue_size > 0) pop (); }

   private:
      NODE *front, *back;
      int queue_size;
};

#endif

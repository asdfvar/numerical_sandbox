#include <iostream>
#include <random>
#include <ctime>
#include <chrono>

#define SIZE 256


long duration () {
   auto now = std::chrono::system_clock::now();
   auto duration = now.time_since_epoch();
   long milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();
   return milliseconds;
}


int main () {

   // 256 bits = 8 * 32 bits
   const long itterations = 1000000000;

   float a[SIZE], b[SIZE], c[SIZE];

   for (int ind = 0; ind < SIZE; ind++) a[ind] = static_cast<float> (rand ());
   for (int ind = 0; ind < SIZE; ind++) b[ind] = static_cast<float> (rand ());
   for (int ind = 0; ind < SIZE; ind++) c[ind] = static_cast<float> (rand ());

   for (int length = 0; length < 8; length++) {
      auto start_time = duration ();
      for (long itt = 0; itt < itterations; itt++)
      {
         for (long ind = 0; ind < length; ind++) c[ind] += a[ind] * b[ind];
      }
      auto end_time = duration ();

      std::cout << "length " << length << " time = " << end_time - start_time << std::endl;
   }
}

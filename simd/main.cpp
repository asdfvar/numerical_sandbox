#include <iostream>
#include <random>
#include <ctime>
#include <chrono>
#include <unistd.h>

#define SIZE 1 * 1024 * 1024

long duration () {
   auto now = std::chrono::system_clock::now();
   auto duration = now.time_since_epoch();
   long milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();
   return milliseconds;
}

int main () {

#if 0
   long page_size = sysconf (_SC_PAGESIZE);
   std::cout << "page size = " << page_size << std::endl;

   const unsigned long big = 8U * 1024U * 1024U * 1024U;
   float *d = new float[big];
   for (unsigned long ind = 0; ind < big; ind++) d[ind] = static_cast<float> (rand ());
#endif

   std::cout << "#!/usr/bin/python3" << std::endl;
   std::cout << std::endl;
   std::cout << "from matplotlib import pyplot as plt" << std::endl;
   std::cout << "import numpy as np" << std::endl;
   std::cout << std::endl;

   unsigned long increments[2] = {1, static_cast<unsigned long> (1024 * 1024 * 0.005)};
   unsigned long itterations[2] = {1000*1000, 100};

   int count = 0;
   int count_ind = 0;

   std::cout << "xy = np.array ([";
   for (int length = 1; length < SIZE; length += increments[count_ind], count++)
   {
      if (count > 40) count_ind = 1;

      float *a = new float[length];
      float *b = new float[length];
      float *c = new float[length];

      for (int ind = 0; ind < length; ind++) a[ind] = static_cast<float> (rand ());
      for (int ind = 0; ind < length; ind++) b[ind] = static_cast<float> (rand ());
      for (int ind = 0; ind < length; ind++) c[ind] = static_cast<float> (rand ());

      long start_time = duration ();

      for (long itt = 0; itt < itterations[count_ind]; itt++)
         for (long ind = 0; ind < length; ind++) c[ind] = a[ind] * b[ind];

      long end_time = duration ();

      float total_time = static_cast<float> (end_time - start_time) / 1000.0f;

      float mb_size = static_cast<float> (length) / 1024.0f / 1024.0f;
      float normalized_time = total_time / length / itterations[count_ind];

      std::cout << "[" << mb_size << ", " << normalized_time << "], " << std::flush;

      delete[] a;
      delete[] b;
      delete[] c;
   }
   std::cout << "])" << std::endl;

   std::cout << std::endl;
   std::cout << "plt.plot (xy[:,0], xy[:,1])" << std::endl;
   std::cout << "plt.show ()" << std::endl;
}

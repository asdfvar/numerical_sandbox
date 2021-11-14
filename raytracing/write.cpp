#include "write.h"
#include "png.h"
#include <iostream>

void write_grayscale_png (float **data, int width, int height, const char *filename)
{

   FILE *fp = fopen (filename, "wb");

   // Initialize write structure
   png_structp png = png_create_write_struct (PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);

   // Initialize info structure
   png_infop info = png_create_info_struct (png);

   // Setup exception handling
   setjmp (png_jmpbuf (png));

   png_init_io (png, fp);

   // Output is 8bit depth, RGBA format.
   png_set_IHDR (
         png,
         info,
         width, height,
         8,
         PNG_COLOR_TYPE_RGB,
         PNG_INTERLACE_NONE,
         PNG_COMPRESSION_TYPE_BASE,
         PNG_FILTER_TYPE_BASE);

   png_write_info (png, info);

   png_bytep png_row_ptr = new png_byte[3*width];

   float max_data_val[3] = {data[0][0], data[1][0], data[2][0]};
   float min_data_val[3] = {data[0][0], data[1][0], data[2][0]};
   for (int channel = 0; channel < 3; channel++) {
      for (int row = 0, ind = 0; row < height; row++) {
         for (int col = 0; col < width; col++, ind++) {
            if (data[channel][ind] > max_data_val[channel]) max_data_val[channel] = data[channel][ind];
            if (data[channel][ind] < min_data_val[channel]) min_data_val[channel] = data[channel][ind];
         }
      }
   }

   for (int row = 0, ind = 0; row < height; row++) {
      for (int col = 0; col < width; col++, ind++) {
         png_row_ptr[3*col + 0] = (unsigned char)((data[0][ind] - min_data_val[0]) / (max_data_val[0] - min_data_val[0]) * 255.0f);
         png_row_ptr[3*col + 1] = (unsigned char)((data[1][ind] - min_data_val[1]) / (max_data_val[1] - min_data_val[1]) * 255.0f);
         png_row_ptr[3*col + 2] = (unsigned char)((data[2][ind] - min_data_val[2]) / (max_data_val[2] - min_data_val[2]) * 255.0f);
      }
      png_write_row (png, png_row_ptr);
   }

   png_write_end (png, NULL);

   delete[] png_row_ptr;

   fclose (fp);

   png_destroy_write_struct (&png, &info);

}

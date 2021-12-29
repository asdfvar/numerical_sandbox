#include "object.h"
#include <iostream>

// Determine if the vector starting at "position" and pointing in "direction" intersect
// the ball by comparing the length from the relation:
// length^2 + ((center - ray_position) \dot direction)^2 = |center - ray_position|^2
// where |direction| = 1.
// with the radius of the ball. The length is the closest distance from the center of the
// ball to the line projected by the vector.
bool Ball::intersect (Ray<float> ray)
{
   ray.direction.normalize ();
   vec::Vector<float> pmx = center - ray.position;

   float length2 = pmx * pmx - ((pmx * ray.direction) * (pmx * ray.direction));
   float length;

   if (length2 > 0.000001f) length = sqrt (length2);
   else                     length = 0.0f;

   // The ray intersects the ball if the nearest point between the ray to the center of the ball
   // is within the radial distance and the center of the ball is in front of the ray
   return length <= radius && pmx * ray.direction > 0.0;
}

// Given the ray starting point 'a' and associated pointing direction of unit length 'd', the
// ball center 'c', with radius length 'r':
// The ray will intersect the ball at point "p = a + d*t" for some value 't'.
// |p - c|^2 = r^2, expanding:
// |(a + d*t) - c|^2 = r^2, expanding:
// |d|^2 *t^2 + 2*(d*a - d*c)*t + (a*a - 2*a*c) = r^2
// since |d|^2 = 1, let
//    B = 2*(d*a - d*c) and
//    C = (a*a - 2*a*c), then
// t = (-B +/- sqrt (B^2 - 4 * C)) / 2   (take the "-" option for the first intersection)
//
// If 'n' is the unit normal at 'p', n = norm (p - c)
// then the new, reflected ray is at point 'p' in the unit direction 'v' which is the result of
// reflecting the ray's direction, 'd', about the normal 'n':
// v = d - 2*(d*n)n

Ray<float> Ball::reflect (Ray<float> incoming_ray)
{
   vec::Vector<float> a = incoming_ray.position;
   vec::Vector<float> d = incoming_ray.direction; d.normalize ();
   vec::Vector<float> c = center;
   float r = radius;

   float B = 2.0 * (d * a - d * c);
   float C = (a * a -  a * c * 2.0);

   float descriminant = B * B - 4.0 * C;
   float t = 0.5 * (-B - sqrt (descriminant));

   vec::Vector<float> p = a + d * t;
   vec::Vector<float> n = p - c; n.normalize ();
   vec::Vector<float> v = d - n * (d * n * 2.0); v.normalize ();

   // Preserve the original, incoming ray's attributes into the reflected ray
   Ray<float> reflected_ray = incoming_ray;

   // Overwrite with the new position and direction of the reflected ray
   reflected_ray.position  = p;
   reflected_ray.direction = v;

   return reflected_ray;
}

// Given the ray starting point 'a' and associated pointing direction of unit length 'd', the
// ball center 'c', with radius length 'r':
// The ray will intersect the ball at point "p = a + d*t" for some value 't'.
// Then the distance would be norm (p - a) = t
float Ball::distance (Ray<float> ray)
{
   vec::Vector<float> a = ray.position;
   vec::Vector<float> d = ray.direction; d.normalize ();
   vec::Vector<float> c = center;
   float r = radius;

   float B = 2.0 * (d * a - d * c);
   float C = a * a -  a * c * 2.0 + c * c - r * r;
   float descriminant = B * B - 4.0 * C;

   float t = 0.5 * (-B - sqrt (descriminant));

   vec::Vector<float> p = a + d * t;

   return t;
}

// TODO:
bool Triangle::intersect (Ray<float> ray)
{
   return false;
}

float Triangle::distance (Ray<float> ray)
{
   vec::Vector<float> a = ray.position;
   vec::Vector<float> d = ray.direction;
   vec::Vector<float> v = d - normal * (d * normal * 2.0f);
   v.normalize ();

   // Find the point of intersection p = a + d*t
   // which happens when p * normal = RHS
   // for t = (RHS - a * normal) / (d * normal)

   float t = (RHS - a * normal) / (d * normal);
   vec::Vector<float> p = a + d * t;
   return t;
}

Ray<float> Triangle::reflect (Ray<float> incoming_ray)
{
   vec::Vector<float> a = incoming_ray.position;
   vec::Vector<float> d = incoming_ray.direction;
   vec::Vector<float> v = d - normal * (d * normal * 2.0f);
   v.normalize ();

   // Find the point of intersection p = a + d*t
   // which happens when p * normal = RHS
   // for t = (RHS - a * normal) / (d * normal)

   float t = (RHS - a * normal) / (d * normal);
   vec::Vector<float> p = a + d * t;

   // Preserve the original, incoming ray's attributes into the reflected ray
   Ray<float> reflected_ray = incoming_ray;

   // Overwrite with the new position and direction of the reflected ray
   reflected_ray.position  = p;
   reflected_ray.direction = v;

   return reflected_ray;
}

template <typename type>
void Object<type>::set_color (vec::Vector<type> color_in)
{
   color.x = color_in.x;
   color.y = color_in.y;
   color.z = color_in.z;
}

template void Object<float>::set_color (vec::Vector<float> color_in);
template void Object<double>::set_color (vec::Vector<double> color_in);

template<typename type>
vec::Vector<type> Object<type>::reflected_color (type gradient)
{
   vec::Vector<type> ray_color;

   ray_color.x = gradient * color.x;
   ray_color.y = gradient * color.y;
   ray_color.z = gradient * color.z;

   return ray_color;
}

template vec::Vector<float> Object<float>::reflected_color (float gradient);
template vec::Vector<double> Object<double>::reflected_color (double gradient);

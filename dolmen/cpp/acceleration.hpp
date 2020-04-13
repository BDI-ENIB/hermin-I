#ifndef DOLMEN_ACCELERATION_HPP
#define DOLMEN_ACCELERATION_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Acceleration : public Sensor
  {
    public :
    Acceleration (int id, std::string name):
    Sensor{id,name}{}

    double getX()
    {
      return x_;
    }

    void setX(double newX)
    {
      x_=newX;
    }

    double getY()
    {
      return y_;
    }

    void setY(double newY)
    {
      y_=newY;
    }

    double getZ()
    {
      return z_;
    }

    void setZ(double newZ)
    {
      z_=newZ;
    }

    void decoding(const std::string data) override
    {
      std::cout<<"test acc";
    }



    private :
    double x_;
    double y_;
    double z_;
  };

}
#endif

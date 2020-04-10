#ifndef DOLMEN_PRESSURE_HPP
#define DOLMEN_PRESSURE_HPP 1
#include <string>
#include"sensor.hpp"

namespace dolmen
{

class Pressure : public Sensor
{
  public :
    Pressure (int id, std::string name):
    Sensor{id, name}{}

    double getPressure()
    {
      return pressure_;
    }

    void setPressure(double newPressure)
    {
      pressure_=newPressure;
    }

    void decoding(const std::string data) override
    {
      std::cout<<"test pressure";
    }

    private :
    double pressure_;
    //int id;
  };
}
#endif

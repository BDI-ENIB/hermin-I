#ifndef DOLMEN_TEMPERATURE_HPP
#define DOLMEN_TEMPERATURE_HPP 1
#include <string>
#include "sensor.hpp"

namespace dolmen
{

class Temperature : public Sensor
{
  public :
    Temperature (int id, std::string name):
    Sensor{id,name}{}

    double getTemperature(){
      return temperature_;
    }

    void setTemperature(double newTemperature){
      temperature_=newTemperature;
    }

    void decoding(const std::string data) override
    {
      std::cout<<"test temperature";
    }

  private :
    double temperature_;
  };
}

#endif

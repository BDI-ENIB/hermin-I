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

    double getTemperature()
    {
      return temperature_;
    }

    void setTemperature(double newTemperature)
    {
      temperature_=newTemperature;
    }

    void decoding(const std::string data) override
    {
      double temperature = 1.0;
      std::string tempstr;
      int id = getID();
      if (data.length() == 7)
      {
        //we check the sign
        (data[2] == '-')? temperature = -temperature : temperature = temperature;
        //we decode each character
        if (isdigit(data[3])) {
          tempstr += data[3];
        }
        if (isdigit(data[4])) {
          tempstr += data[4];
        }

        tempstr += ".";

        if (isdigit(data[5])) {
          tempstr += data[5];
        }
        if (isdigit(data[6])) {
          tempstr += data[6];
        }

        temperature = temperature * std::stod(tempstr);

        setTemperature(temperature);

        std::cout << "\ntemperature = " << temperature;
      }
      else
      {
        std::cout << "\nerror: bad data format";
      }
    }

    private :
    double temperature_;
  };
}

#endif

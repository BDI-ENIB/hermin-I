#ifndef DOLMEN_TEMPERATURE_HPP
#define DOLMEN_TEMPERATURE_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{
  class Temperature : public Sensor
  {
    public :
    Temperature (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Temperature";
    }

    int getNbAttr() override
    {
      return 1;
    }
  };
}

#endif

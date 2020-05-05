#ifndef DOLMEN_PRESSURE_HPP
#define DOLMEN_PRESSURE_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Pressure : public Sensor
  {
    public :
    Pressure (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Pressure";
    }

    int getNbAttr() override
    {
      return 1;
    }


  };
}
#endif

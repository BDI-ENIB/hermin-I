#ifndef DOLMEN_ALTITUDE_HPP
#define DOLMEN_ALTITUDE_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Altitude : public Sensor
  {
    public :

    Altitude (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Altitude";
    }

    int getNbAttr() override
    {
      return 1;
    }
  };
}
#endif

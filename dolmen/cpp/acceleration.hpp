#ifndef DOLMEN_ACCELERATION_HPP
#define DOLMEN_ACCELERATION_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{
  class Acceleration : public Sensor
  {
    public :
    Acceleration (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Accelerometer";
    }

    int getNbAttr() override
    {
      return 3;
    }
  };
}

#endif

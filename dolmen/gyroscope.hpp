#ifndef DOLMEN_GYROSCOPE_HPP
#define DOLMEN_GYROSCOPE_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{
  class Gyroscope : public Sensor
  {
    public :
    Gyroscope (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Gyroscope";
    }

    int getNbAttr() override
    {
      return 3;
    }
  };
}

#endif

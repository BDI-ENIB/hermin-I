#ifndef DOLMEN_GPS_HPP
#define DOLMEN_GPS_HPP 1

#include <string>
#include <vector>
#include "sensor.hpp"

namespace dolmen
{

  class Gps : public Sensor
  {
    public :
    Gps (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Gps";
    }

    int getNbAttr() override
    {
      return 6;
    }
  };
}
#endif

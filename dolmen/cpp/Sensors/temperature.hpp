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

    Sensor* Clone() const
    {
      return new Temperature(*this);
    }

    std::map<std::string, double> decoding(const std::string data) override;
  };
}

#endif

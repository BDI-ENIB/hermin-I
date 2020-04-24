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

    void decoding(const std::string data) override;

    std::map<std::string, double> getValue() override
    {
      std::map<std::string, double> sensorData;
      sensorData.insert(std::pair<std::string, double>("temperature", temperature_));
      return sensorData;
    }

    std::string getColumnIdentifiers() override
    {
      std::string identifier = "Temperature";
      return identifier;
    }

    int getNbAttr() override
    {
      return 1;
    }

  private:
    double temperature_;
  };
}

#endif

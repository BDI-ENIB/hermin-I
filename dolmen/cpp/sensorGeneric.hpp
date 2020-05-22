#ifndef DOLMEN_SENSOR_GENERIC_HPP
#define DOLMEN_SENSOR_GENERIC_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class SensorGeneric : public Sensor
  {
    public :
    SensorGeneric (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      //change this name by the name which will appear in the .csv column
      return "SensorGeneric";
    }

    int getNbAttr() override
    {
      //change this number by the number of returned values of your sensor
      return 1;
    }
  };
}

#endif





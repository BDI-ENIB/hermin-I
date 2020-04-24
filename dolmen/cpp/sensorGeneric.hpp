#ifndef DOLMEN_SENSOR_GENERIC_HPP
#define DOLMEN_SENSOR_GENERIC_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class SensorGeneric : public Sensor
  {
    public :
    SensorGeneric (int id, std::string name):
    Sensor{id,name}{}

    ~SensorGeneric(){}

    double getSensorGeneric()
    {
      return sensorGeneric_;
    }

    void setSensorGeneric(double newSensorGeneric)
    {
      sensorGeneric_=newSensorGeneric;
    }

    void decoding(const std::string data) override
    {
      int id = getID();
      if (data.length() == /*to complete*/ && data[/*to complete*/] == ';')
      {
        //
      }
      else
      {
        std::cout << "\nerror: bad data format";
      }
    }

    std::string toCsv() override
    {
      std::string dataTxt;
      dataTxt += std::to_string(sensorGeneric_);
      dataTxt += ",";
      return dataTxt;
    }

    private :
    double sensorGeneric_;
  };
}

#endif

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
      double sensorGeneric = 1.0;
      std::string tempstr;
      int id = getID();
      if (data.length() == 8 && data[7] == ';')
      {
        //we check the sign
        (data[2] == '-')? sensorGeneric = -sensorGeneric : sensorGeneric = sensorGeneric;
        //we decode each character
        if (isdigit(data[3])) {
          tempstr += data[3];
        }
        if (isdigit(data[4])) {
          tempstr += data[4];
        }

        tempstr += ".";

        if (isdigit(data[5])) {
          tempstr += data[5];
        }
        if (isdigit(data[6])) {
          tempstr += data[6];
        }

        sensorGeneric = sensorGeneric * std::stod(tempstr);

        setSensorGeneric(sensorGeneric);

        std::cout << "\nsensorGeneric = " << sensorGeneric;
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

#ifndef DOLMEN_ALTITUDE_HPP
#define DOLMEN_ALTITUDE_HPP 1

#include <string>
#include <math.h>
#include "sensor.hpp"

namespace dolmen
{

  class Altitude : public Sensor
  {
    public :
    Altitude (int id, std::string name):
    Sensor{id,name}{}

    ~Altitude(){}

    double getAltitude(){
      return altitude_;
    }

    void setAltitude(double newAltitude){
      altitude_=newAltitude;
    }

    void decoding(const std::string data) override
    {
      //altitude have to be calculated from other sensors's datas
      double altitude = 0;

      //with the pressure

      //double pressure = dolmen::Pressure::getPressure(); //must be in hPa
      double pressure = 0.0;

      double p0 = 1013.25;
      double g = 9.81;
      double Cp = 1006.0;
      double T0 = 20.0;

      altitude = log(pressure/p0)*((2*Cp*T0)/(-7*g));

      setAltitude(altitude);

      std::cout << "\naltitude = " << altitude;
    }

    std::string toCsv() override
    {
      std::string dataTxt;
      dataTxt += std::to_string(altitude_);
      dataTxt += ",";
      return dataTxt;
    }

    private :
    double altitude_;
  };

}
#endif

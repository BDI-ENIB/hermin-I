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

    double getAltitude(){
      return altitude_;
    }

    void setAltitude(double newAltitude){
      altitude_=newAltitude;
    }

    void decoding(const std::string data) override
    {
      //altitude have to be calculated from other sensors's datas
      int altitude = 0;

      //with the pressure

      double pressure = Pressure::getPressure(); //must be in hPa

      double p0 = 1013.25;
      double g = 9.81;
      double Cp = 1006.0;
      double T0 = 20.0;

      altitude = log(pressure/p0)*((2*Cp*T0)/(-7*g));

      setAltitude(altitude)

      std::cout << "\naltitude = " << altitude;
    }

    private :
    double altitude_;
  };

}
#endif

#include "altitude.hpp"

namespace dolmen
{
  Altitude::Altitude (int id, std::string name):Sensor{id,name}{}

  void Altitude::decoding(const std::string data)
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

    //altitude = log(pressure/p0)*((2*Cp*T0)/(-7*g));
    altitude = 666.666;

    //inserting the processed datas into the sensor data container
    insert("altitude",altitude);

  }


} /* dolmen */

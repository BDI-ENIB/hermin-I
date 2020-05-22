#include "sensorGeneric.hpp"

namespace dolmen
{
  SensorGeneric::SensorGeneric (int id, std::string name):Sensor{id,name}{}

  void SensorGeneric::decoding(const std::string data)
  {
    //insert here the decoding method of your sensor
  }
} /* dolmen */
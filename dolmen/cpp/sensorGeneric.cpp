#include "sensorGeneric.hpp"

namespace dolmen
{
  sensorGeneric::sensorGeneric (int id, std::string name):Sensor{id,name}{}

  void sensorGeneric::decoding(const std::string data)
  {
    //insert here the decoding method of your sensor
  }
} /* dolmen */
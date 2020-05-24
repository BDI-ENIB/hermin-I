#include "sensorGeneric.hpp"

/*THIS FILS IS A BLANK EXAMPLE, YOU'LL NEED TO COMPLETE IT IF YOU WANT YOUR SENSOR TO WORK*/

namespace dolmen
{
  SensorGeneric::SensorGeneric (int id, std::string name):Sensor{id,name}{}

  void SensorGeneric::decoding(const std::string data)
  {
    //insert here the decoding method of your sensor, you can check others sensors to see how we created the previous ones
  }
} /* dolmen */
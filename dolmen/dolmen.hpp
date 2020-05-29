#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <memory>
#include <time.h>

//#include "sensorInit.hpp"

#include "factorySensor.hpp"
#include "sensor.hpp"
//insert here your sensors hpp files
#include "temperature.hpp"
#include "gyroscope.hpp"
#include "acceleration.hpp"
#include "altitude.hpp"
#include "gps.hpp"
#include "pressure.hpp"
#include "time.hpp"


namespace dolmen
{

  class Dolmen
  {
  private:
    /* data */

  public:

    Dolmen();

    ~Dolmen(){}

    std::string decoding(std::string data, std::map<int, dolmen::Sensor*> sensorList);

  };
} /* dolmen */

#endif

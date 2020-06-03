#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <memory>
#include <time.h>

//including software hpp files
#include "factorySensor.hpp"
#include "sensor.hpp"
#include "time.hpp"
//including sensors hpp files
//insert here your sensors hpp files
#include "temperature.hpp"
#include "gyroscope.hpp"
#include "acceleration.hpp"
#include "altitude.hpp"
#include "gps.hpp"
#include "pressure.hpp"



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

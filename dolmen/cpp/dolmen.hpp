#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <memory>

#include "factorySensor.hpp"
#include "temperature.hpp"

namespace dolmen
{

  class Dolmen
  {
  private:
    /* data */

  public:

    Dolmen();

    ~Dolmen(){}

    //std::string decoding(std::string data, std::map<int, std::unique_ptr<dolmen::Sensor>> sensors_list);
    std::string decoding(std::string data, std::map<int, dolmen::Sensor*> sensorList);

  };
} /* dolmen */

#endif

#ifndef DOLMEN_TIME_HPP
#define DOLMEN_TIME_HPP 1

#include <string>
#include <time.h>

#include "sensor.hpp"

namespace dolmen
{
  class Time : public Sensor
  {
    public :
    Time (int id, std::string name);

    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
      return "Time";
    }

    int getNbAttr() override
    {
      return 1;
    }

    time_t starting = time(0);
  };

}

#endif
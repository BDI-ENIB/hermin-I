/*#ifndef DOLMEN_CONFIGURATION_HPP
#define DOLMEN_CONFIGURATION_HPP 1

#include <string>
#include <vector>
#include <memory>
#include <iostream>

#include "sensor.hpp"
#include "temperature.hpp"
#include "pressure.hpp"
#include "acceleration.hpp"
#include "gps.hpp"
#include "gyroscope.hpp"
#include "altitude.hpp"

namespace dolmen
{

  class Configuration
  {
    public :

    Configuration();

    ~Configuration(){}

    std::vector<std::unique_ptr<dolmen::Sensor>> getSensors_config()
    {
      return std::move(sensors_config);
    }

    void setSensors_config(std::vector<std::unique_ptr<dolmen::Sensor>> config)
    {
      sensors_config = std::move(config);
    }

    std::vector<std::unique_ptr<dolmen::Sensor>> import_config();

    void export_config(std::vector<std::unique_ptr<dolmen::Sensor>> sensors_config);

    private :
    std::vector<std::unique_ptr<dolmen::Sensor>> sensors_config;
  };
}

#endif*/

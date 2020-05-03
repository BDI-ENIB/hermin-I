#ifndef DOLMEN_FACTORY_SENSOR_HPP
#define DOLMEN_FACTORY_SENSOR_HPP 1

#include "sensor.hpp"

namespace dolmen
{
  //We use a factory pattern, to be able to upgrade the program later, to automation the sensor creation
  class FactorySensor
  {
  public:
    static std::map<std::string, Sensor*> m_map;

  public:
    //FactorySensor ();
    //~FactorySensor ();

    //Function to associate key and prototype
    static void Register(const std::string& key,Sensor* obj);


    //Function to create objects
    Sensor* Create(const std::string& key) const;
  };
} /* dolmen */

#endif

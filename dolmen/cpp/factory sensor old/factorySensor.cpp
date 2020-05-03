#include "factorySensor.hpp"

namespace dolmen
{
  std::map<std::string,Sensor*> FactorySensor::m_map = std::map<std::string,Sensor*>();

  //Function to associate key and prototype

  void FactorySensor::Register(const std::string& key,Sensor* obj)
  {
    //if the key doesn't already exixts
    if(m_map.find(key)==m_map.end())
    {
      //adding object on the map
      m_map[key]=obj;
    }
  }

  //Function to create objects
  Sensor* FactorySensor::Create(const std::string& key) const
  {
    Sensor* tmp=0;
    std::map<std::string, Sensor*>::const_iterator it=m_map.find(key);

    //if iterator != map.end(), this means the key has been found
    if(it!=m_map.end())
    {
      tmp=((*it).second)->Clone();
    }

    //if key isn't found, we can throw an exception
    if (it==m_map.end())
    {
      std::cout << "error to add later";
    }

    return tmp;
  }
} /* dolmen */

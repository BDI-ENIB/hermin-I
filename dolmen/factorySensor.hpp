#ifndef DOLMEN_FACTORY_SENSOR_HPP
#define DOLMEN_FACTORY_SENSOR_HPP 1

#include <cassert>
#include <unordered_map>
#include <string>
#include <functional>
#include <memory>
#include <iostream>

#include "sensor.hpp"

namespace dolmen
{
  //We use a factory pattern, to be able to upgrade the program later (automation of the sensor creation)
  template <class Key, class Object, class... Args>
  class FactorySensor
  {
  public:
    using Creator = std::function<Object(Args...)>;

    void registe(Key const& key, Creator const& creator)
    {
      assert(m_creators.count(key) == 0);
      assert(creator);
      m_creators.emplace(key, creator);
    }

    Object create(Key const& key, Args &&... args)
    {
      assert(m_creators.count(key) == 1);
      assert(m_creators[key]);
      return m_creators[key](std::forward<Args>(args)...);
    }

  private:
    std::unordered_map<Key, Creator> m_creators;
  };
} /* dolmen */

#endif

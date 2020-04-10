#ifndef DOLMEN_SENSORS_HPP
#define DOLMEN_SENSORS_HPP 1
#include <string>
#include <iostream>

namespace dolmen
{

  class Sensor
  {
    public :
      Sensor (int id, std::string name):id_{id},name_{name}
      {}

      virtual ~Sensor()
      {
        //
      }

      virtual void decoding(const std::string data) = 0;

      int getID()
      {
        return id_;
      }

      std::string getName()
      {
        return name_;
      }

    private :
      int id_;
      std::string name_;
  };
}

#endif

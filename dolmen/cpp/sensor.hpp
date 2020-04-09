#ifndef DOLMEN_SENSORS_HPP
#define DOLMEN_SENSORS_HPP 1
#include <string>

namespace dolmen
{

  class Sensor
  {
    public :
      Sensor (int id, std::string name)
      {
        int id_=id;
        std::string name_=name;
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

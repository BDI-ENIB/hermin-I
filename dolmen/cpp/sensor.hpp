#ifndef DOLMEN_SENSORS_HPP
#define DOLMEN_SENSORS_HPP 1
#include <string>
#include <iostream>

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

      virtual ~Sensor()
      {
        //
      }

      virtual void decoding(const std::string data) = 0;

      int getID()
      {
        std::cout << " j'affiche l'id ";
        std:: cout << id_;
        return id_;
      }

      std::string getName()
      {
        std::cout << " j'affiche le nom ";
        std:: cout << name_;
        return name_;
      }

    private :
      int id_;
      std::string name_;
  };
}

#endif

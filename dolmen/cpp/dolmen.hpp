#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>

#include "temperature.hpp"
#include "pressure.hpp"


namespace dolmen
{

  class Dolmen
  {
  private:
    /* data */

  public:

    void decoding(std::string data, std::vector<Sensor> sensors_list)
    {
      //reading data to determine the sensor
      int id = data[0] + data[1];
      bool found = false;

      for (auto& elem : sensors_list)
      {
        if (elem.getID() == id)
        {
          elem.decoding(data);
          found = true;
          break;
        }
      }
      if (found == false)
      {
        //error to add
        std::cout<<"error: unknown sensor";
      }
    }
  };
} /* dolmen */

#endif

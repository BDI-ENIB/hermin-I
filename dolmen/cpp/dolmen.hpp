#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>

#include "sensors.hpp"

namespace dolmen
{

  class Dolmen
  {
  private:
    /* data */

  public:

    void decoding(std::string data, std::vector<std::string> ids)
    {
      //reading data to determine the sensor
      std::string id = (char)data[0] + (char)data[1];
      int len = (ids.size())/2;

      for (size_t i = 0; i < len; i++)
      {
        if (ids[i] == id)
        {
          //
          std::string name = ids[i+1];
          name.decoding(data);
        }
        if (i == len && ids[i] != id)
        {
          //error to add
          std::cout<<"error: unknown sensor";
        }
      }
    }



  };
} /* dolmen */

#endif

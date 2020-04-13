#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>

#include "temperature.hpp"
#include "pressure.hpp"
#include "acceleration.hpp"
#include "gps.hpp"
#include "gyroscope.hpp"
#include "altitude.hpp"


namespace dolmen
{

  class Dolmen
  {
  private:
    /* data */

  public:

    void decoding(std::string data, std::vector<std::unique_ptr<dolmen::Sensor>> sensors_list)
    {
      //reading data to determine the sensor
      std::cout << "\n j'entre dans dolmen::decoding \n";

      //reading the sensor id
      std::string idstr;
      if (isdigit(data[0])) {
        idstr += data[0];
      }
      if (isdigit(data[1])) {
        idstr += data[1];
      }

      //converting the sensor id into an int
      int id = std::stoi(idstr);

      //std::cout << "\n id chaine = " << idstr << "\n";
      //std::cout << "\n id int = " << id << "\n";


      bool found = false;
      for (const auto& elem : sensors_list)
      {
        //std::cout << elem->getID() << "=" << id << "?\n";
        if (elem->getID() == id)
        {
          elem->decoding(data);
          found = true;
          std::cout << "\nsensor found: " << id;
          break;
        }
      }
      if (found == false)
      {
        //error to add
        std::cout<<"\n ---error: unknown sensor--- \n";
      }
    }
  };
} /* dolmen */

#endif

#ifndef DOLMEN_DOLMEN_HPP
#define DOLMEN_DOLMEN_HPP 1

#include <vector>
#include <iostream>
#include <string>
#include <fstream>

#include "configuration.hpp"

namespace dolmen
{

  class Dolmen
  {
  private:
    /* data */

  public:

    Dolmen ()
    {
      //
    }

    ~Dolmen()
    {
      //
    }

    std::string decoding(std::string data, std::vector<std::unique_ptr<dolmen::Sensor>> sensors_list)
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

      std::string dataTxt;

      bool found = false;
      for (const auto& elem : sensors_list)
      {
        //std::cout << elem->getID() << "=" << id << "?\n";
        if (elem->getID() == id)
        {
          elem->decoding(data);
          dataTxt += elem->getName();
          dataTxt += ",";
          dataTxt += elem->toCsv();
          dataTxt += ",";
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

      return dataTxt;
    }
  };
} /* dolmen */

#endif

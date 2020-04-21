#include <fstream>
#include <iostream>
#include <string>

#include "configuration.hpp"

namespace dolmen
{
  Configuration::Configuration(){}

  std::vector<std::unique_ptr<dolmen::Sensor>> Configuration::import_config()
  {
    std::cout << "\n entree import config";
    std::ifstream config("config.txt");
    std::vector<std::unique_ptr<dolmen::Sensor>> sensors_config;

    if(config)
    {
      std::cout << "\nyesconfig \n";
      //each line is a measurement of the rocket, with datas of each sensor
      std::string line;
      while(std::getline(config,line))
      {
        std::string tag = line.substr(0,7);
        std::cout << "\n" << line << " tag " << tag;
        if (tag == "SENSOR;")
        {
          std::string id;
          std::string name;
          std::string sensor;
          int i = 0;
          std::string ministring;
          for (auto& letter : line)
          {
            ministring += letter;
            if (letter == ';')
            {
              i += 1;
              if (i == 2)
              {
                //this is the ; just after the id
                id = ministring;
                std::cout << "\n affichage id: " << id;
              }
              if (i == 3)
              {
                //this is the ; just after the sensor name
                name = ministring;
                std::cout << "\n affichage name: " << name;
              }
              if (i == 4)
              {
                //this is the ; just after the sensor code location
                sensor = ministring;
                std::cout << "\n affichage sensor: " << sensor;
              }
              ministring = "";
            }
            sensors_config.push_back(std::make_unique<dolmen::Temperature> (01, "bob"));
          }
        }
      }
    }
    return std::move(sensors_config);
  }

  void Configuration::export_config(std::vector<std::unique_ptr<dolmen::Sensor>> sensors_config)
  {
    //
  }
} /* dolmen */

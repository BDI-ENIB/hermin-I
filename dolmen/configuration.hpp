#ifndef DOLMEN_CONFIGURATION_HPP
#define DOLMEN_CONFIGURATION_HPP 1

#include <string>
#include <vector>
#include <memory>
#include <iostream>
#include <fstream>

namespace dolmen
{
  std::map<std::string, std::string> import_config(std::string filename)
  {
    //opening the configuration folder
    std::ifstream config(filename);

    //creating an empty map
    std::map<std::string, std::string> config_map;

    if(config)
    {
      //checking the lines and reading their content
      std::string line;
      int line_bacon = 0;
      while(std::getline(config,line))
      {
        line_bacon += 1;
        if (line_bacon == 1)
        {
          //first line is to check if we are allowed to decode
          config_map.insert(std::make_pair("decoding_authorised",line));
        }
        if (line_bacon == 2)
        {
          //second line is to check if we are in online or offline mode
          config_map.insert(std::make_pair("mode",line));
        }
        if (line_bacon == 3)
        {
          //third line is to read the path to the trame.txt file
          config_map.insert(std::make_pair("data_path",line));
        }
        //adding new lines in the config file goes there
    }
  }
  return config_map;
  }
}



#endif

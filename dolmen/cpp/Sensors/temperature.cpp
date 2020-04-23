#include "temperature.hpp"

namespace dolmen
{
  Temperature::Temperature (int id, std::string name):Sensor{id,name}{}

  std::map<std::string, double> Temperature::decoding(const std::string data) override
  {
    std::map<std::string name, double value> map;
    double temperature = 1.0;
    std::string tempstr;
    int id = getID();
    if (data.length() == 8 && data[7] == ';')
    {
      //we check the sign
      (data[2] == '-')? temperature = -temperature : temperature = temperature;
      //we decode each character
      if (isdigit(data[3])) {
        tempstr += data[3];
      }
      if (isdigit(data[4])) {
        tempstr += data[4];
      }

      tempstr += ".";

      if (isdigit(data[5])) {
        tempstr += data[5];
      }
      if (isdigit(data[6])) {
        tempstr += data[6];
      }

      temperature = temperature * std::stod(tempstr);

      std::cout << "\ntemperature = " << temperature;
      map.insert(std::pair<std::string, double>("temperature",temperature));
      return map
    }
    else
    {
      std::cout << "\nerror: bad data format";
    }
  }
} /* dolmen */

#include "pressure.hpp"

namespace dolmen
{
  Pressure::Pressure (int id, std::string name):Sensor{id,name}{}


  void Pressure::decoding(const std::string data)
  {
    //initialising the values
    double pressure = 1.0;
    std::string presstr;
    int id = getID();
    if (data.length() == 8 && data[7] == ';')
    {
      //we check the sign
      (data[2] == '-')? pressure = -pressure : pressure = pressure;
      //we decode each character
      if (isdigit(data[3])) {
        presstr += data[3];
      }
      if (isdigit(data[4])) {
        presstr += data[4];
      }

      presstr += ".";

      if (isdigit(data[5])) {
        presstr += data[5];
      }
      if (isdigit(data[6])) {
        presstr += data[6];
      }

      //we adjust the pressure if it's positive or negative
      pressure = pressure * std::stod(presstr);

      //inserting the processed datas into the sensor data container
      insert("pressure",pressure);

    }
    else
    {
      //if there is a problem avoiding to decode the data, we insert the value 0.0, and the name become "gyroscope_error"
      std::cout << "\nerror: bad data format";
      insert("pressure_error", 0.0);
    }
  }

} /* dolmen */

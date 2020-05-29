#include "pressure.hpp"

namespace dolmen
{
  Pressure::Pressure (int id, std::string name):Sensor{id,name}{}


  void Pressure::decoding(const std::string data)
  {
    //pressure is in Pa
    //initialising the values
    double pressure = 1.0;
    std::string presstr;
    int id = getID();
    if (data.length() == 9 && data[8] == ';')
    {
      //we decode each character
      if (isdigit(data[2])) 
      {
        presstr += data[2];
      }
      if (isdigit(data[3])) 
      {
        presstr += data[3];
      }
      if (isdigit(data[4])) 
      {
        presstr += data[4];
      }
      if (isdigit(data[5])) 
      {
        presstr += data[5];
      }
      if (isdigit(data[6])) 
      {
        presstr += data[6];
      }
      if (isdigit(data[7])) 
      {
        presstr += data[7];
      }

      pressure = std::stod(presstr);

      //inserting the processed datas into the sensor data container
      insert("pressure (Pa)",pressure);

    }
    else
    {
      //if there is a problem avoiding to decode the data, we insert the value 0.0, and the name become "gyroscope_error"
      std::cout << "\nerror: bad data format" << id;
      insert("pressure_error", 0.0);
    }
  }

} /* dolmen */

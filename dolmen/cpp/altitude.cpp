#include "altitude.hpp"
#include <tgmath.h>

namespace dolmen
{
  Altitude::Altitude (int id, std::string name):Sensor{id,name}{}

  void Altitude::decoding(const std::string data)
  {
    //the altitude sensor use the data from a pressure sensor
    //initialising the values
    double altitude = 0.0;
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

      if (pressure < 0.0)
      {
        std::cout << "error: negative pressure, cannot calculate altitude";
      }
    
      //setting up constants
      double h0 = 0; //height of the launching site
      double p0 = 1013.25; //presure of the launching site
      double g = 9.81; //gravitational constant
      double T0 = 288.15; //temperature of the launching site
      double R = 8.3144598; //universal gas constant
      double M = 0.0289644; //molar mass of Earth's air

      //using the barometric formula (this formula is accurate for low altitudes, under 15-20km)
      altitude = h0-((log((pressure/100)/p0)*R*T0)/(g*M));

      //inserting the processed datas into the sensor data container
      insert("altitude (m)",altitude);
    }
    else
    {
      //if there is a problem avoiding to decode the data, we insert the value 0.0, and the name become "gyroscope_error"
      std::cout << "\nerror: bad data format" << id;
      insert("altitude_error",0.0);
    }
  }
} /* dolmen */

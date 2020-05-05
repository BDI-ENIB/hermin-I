#include "gyroscope.hpp"

namespace dolmen
{
  Gyroscope::Gyroscope (int id, std::string name):Sensor{id,name}{}

  void Gyroscope::decoding(const std::string data)
  {
    int id = getID();
    double gyrX = 1.0;
    double gyrY = 1.0;
    double gyrZ = 1.0;
    std::string strX;
    std::string strY;
    std::string strZ;


    if (data.length() == 18 && data[17] == ';')
    {
      //X
      //we check the sign
      (data[2] == '-')? gyrX = -gyrX : gyrX = gyrX;
      //we decode each character
      if (isdigit(data[3])) {
        strX += data[3];
      }
      if (isdigit(data[4])) {
        strX += data[4];
      }

      strX += ".";

      if (isdigit(data[5])) {
        strX += data[5];
      }
      if (isdigit(data[6])) {
        strX += data[6];
      }

      gyrX = gyrX * std::stod(strX);

      //Y
      //we check the sign
      (data[7] == '-')? gyrY = -gyrY : gyrY = gyrY;
      //we decode each character
      if (isdigit(data[8])) {
        strY += data[8];
      }
      if (isdigit(data[9])) {
        strY += data[9];
      }

      strY += ".";

      if (isdigit(data[10])) {
        strY += data[10];
      }
      if (isdigit(data[11])) {
        strY += data[11];
      }

      gyrY = gyrY * std::stod(strY);

      //Z
      //we check the sign
      (data[12] == '-')? gyrZ = -gyrZ : gyrZ = gyrZ;
      //we decode each character
      if (isdigit(data[13])) {
        strZ += data[13];
      }
      if (isdigit(data[14])) {
        strZ += data[14];
      }

      strZ += ".";

      if (isdigit(data[15])) {
        strZ += data[15];
      }
      if (isdigit(data[16])) {
        strZ += data[16];
      }

      gyrZ = gyrZ * std::stod(strZ);

      //inserting the processed datas into the sensor data container
      insert("gyroscope_X", gyrX);
      insert("gyroscope_Y", gyrY);
      insert("gyroscope_Z", gyrZ);

    }
    else
    {
      //if there is a problem avoiding to decode the data, we insert the value 0.0, and the name become "gyroscope_error"
      std::cout << "\nerror: bad data format";
      insert("gyroscope_error_X", 0.0);
      insert("gyroscope_error_Y", 0.0);
      insert("gyroscope_error_Z", 0.0);
    }
  }

} /* dolmen */

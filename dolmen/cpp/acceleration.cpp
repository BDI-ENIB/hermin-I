#include "acceleration.hpp"

namespace dolmen
{
  Acceleration::Acceleration (int id, std::string name):Sensor{id,name}{}

  void Acceleration::decoding(const std::string data)
  {
    int id = getID();
    double accX = 1.0;
    double accY = 1.0;
    double accZ = 1.0;
    std::string strX;
    std::string strY;
    std::string strZ;


    if (data.length() == 18 && data[17] == ';')
    {
      //X
      //we check the sign
      (data[2] == '-')? accX = -accX : accX = accX;
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

      accX = accX * std::stod(strX);

      //Y
      //we check the sign
      (data[7] == '-')? accY = -accY : accY = accY;
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

      accY = accY * std::stod(strY);

      //Z
      //we check the sign
      (data[12] == '-')? accZ = -accZ : accZ = accZ;
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

      accZ = accZ * std::stod(strZ);

      //inserting the processed datas into the sensor data container
      insert("accelerometer_X", accX);
      insert("accelerometer_Y", accY);
      insert("accelerometer_Z", accZ);

    }
    else
    {
      //if there is a problem avoiding to decode the data, we insert the value 0.0, and the name become "gyroscope_error"
      std::cout << "\nerror: bad data format";
      insert("accelerometer_error_X", 0.0);
      insert("accelerometer_error_Y", 0.0);
      insert("accelerometer_error_Z", 0.0);
    }
  }

} /* dolmen */

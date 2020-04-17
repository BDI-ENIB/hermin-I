#ifndef DOLMEN_GYROSCOPE_HPP
#define DOLMEN_GYROSCOPE_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Gyroscope : public Sensor
  {
    public :
    Gyroscope (int id, std::string name):
    Sensor{id,name}{}

    ~Gyroscope(){}

    double getX()
    {
      return x_;
    }

    void setX(double newX)
    {
      x_=newX;
    }

    double getY()
    {
      return y_;
    }

    void setY(double newY){
      y_=newY;
    }

    double getZ(){
      return z_;
    }

    void setZ(double newZ)
    {
      z_=newZ;
    }

    void decoding(const std::string data) override
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

        setX(gyrX);

        std::cout << "\n gyrX = " << gyrX;

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

        setX(gyrY);

        std::cout << "\n gyrY = " << gyrY;

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

        setX(gyrZ);

        std::cout << "\n gyrZ = " << gyrZ;

      }
      else
      {
        std::cout << "\nerror: bad data format";
      }
    }

    std::string toCsv() override
    {
      std::string dataTxt;
      dataTxt += "name";
      dataTxt += ",";
      return dataTxt;
    }

    private :
    double x_;
    double y_;
    double z_;
  };

}
#endif

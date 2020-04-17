#ifndef DOLMEN_ACCELERATION_HPP
#define DOLMEN_ACCELERATION_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Acceleration : public Sensor
  {
    public :
    Acceleration (int id, std::string name):
    Sensor{id,name}{}

    ~Acceleration(){}

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

    void setY(double newY)
    {
      y_=newY;
    }

    double getZ()
    {
      return z_;
    }

    void setZ(double newZ)
    {
      z_=newZ;
    }

    void decoding(const std::string data) override
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

        setX(accX);

        std::cout << "\n accX = " << accX;

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

        setX(accY);

        std::cout << "\n accY = " << accY;

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

        setX(accZ);

        std::cout << "\n accZ = " << accZ;

        setX(accX);
        setY(accY);
        setY(accY);

      }
      else
      {
        std::cout << "\nerror: bad data format";
      }
    }

    std::string toCsv() override
    {
      std::string dataTxt;
      dataTxt += std::to_string(x_);
      dataTxt += ",";
      dataTxt += std::to_string(y_);
      dataTxt += ",";
      dataTxt += std::to_string(z_);
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

#ifndef DOLMEN_PRESSURE_HPP
#define DOLMEN_PRESSURE_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Pressure : public Sensor
  {
    public :
    Pressure (int id, std::string name):
    Sensor{id, name}{}

    ~Pressure(){}

    double getPressure()
    {
      return pressure_;
    }

    void setPressure(double newPressure)
    {
      pressure_=newPressure;
    }

    void decoding(const std::string data) override
    {
      double pressure = 1.0;
      std::string presstr;
      int id = getID();
      std::cout << "test" << data[7];
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

        pressure = pressure * std::stod(presstr);

        setPressure(pressure);

        std::cout << "\npressure = " << pressure;
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
    double pressure_;
    //int id;
  };
}
#endif

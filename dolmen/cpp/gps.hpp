#ifndef DOLMEN_GPS_HPP
#define DOLMEN_GPS_HPP 1

#include <string>
#include "sensor.hpp"

namespace dolmen
{

  class Gps : public Sensor
  {
    public :
    Gps (int id, std::string name):
    Sensor{id, name}{}

    double getLatitude()
    {
      return latitude_;
    }

    void setLatitude(double newLatitude)
    {
      latitude_=newLatitude;
    }

    double getLongitude()
    {
      return longitude_;
    }

    void setLongitude(double newLongitude)
    {
      longitude_=newLongitude;
    }

    void decoding(const std::string data) override
    {
      if (data.length() == 21 && data[20] == ';')
      {
        int id = getID();

        //latitude

        //we consider being in the north hemisphere (0-90°N)
        int latDeg = 0;
        int latMin = 0;
        double latSec = 0.0;
        std::string latDegStr;
        std::string latMinStr;
        std::string latSecStr;

        //we decode each character for the °

        if (isdigit(data[2])) {
          latDegStr += data[2];
        }
        if (isdigit(data[3])) {
          latDegStr += data[3];
        }
        latDeg = std::stoi(latDegStr);
        //setTemperature(latDeg);
        std::cout << "\n latDeg = " << latDeg;


        //we decode each character for the '

        if (isdigit(data[4])) {
          latMinStr += data[4];
        }
        if (isdigit(data[5])) {
          latMinStr += data[5];
        }
        latMin = std::stoi(latMinStr);
        //setTemperature(latDeg);
        std::cout << "\n latMin = " << latMin;


        //we decode each character for the "
        if (isdigit(data[6])) {
          latSecStr += data[6];
        }
        if (isdigit(data[7])) {
          latSecStr += data[7];
        }

        latSecStr += ".";

        if (isdigit(data[8])) {
          latSecStr += data[8];
        }
        if (isdigit(data[9])) {
          latSecStr += data[9];
        }
        latSec = std::stod(latSecStr);
        //setTemperature(latSec);
        std::cout << "\n latSec = " << latSec;


        //longitude

        int lonDeg = 1;
        int lonMin = 0;
        double lonSec = 0.0;
        std::string lonDegStr;
        std::string lonMinStr;
        std::string lonSecStr;

        //we decode each character for the °

        //we check the sign
        (data[10] == '-')? lonDeg = -lonDeg : lonDeg = lonDeg;
        //we decode
        if (isdigit(data[11])) {
          lonDegStr += data[11];
        }
        if (isdigit(data[12])) {
          lonDegStr += data[12];
        }
        if (isdigit(data[13])) {
          lonDegStr += data[13];
        }
        lonDeg = lonDeg * std::stoi(lonDegStr);
        //setTemperature(latDeg);
        std::cout << "\n lonDeg = " << lonDeg;


        //we decode each character for the '

        if (isdigit(data[14])) {
          lonMinStr += data[14];
        }
        if (isdigit(data[15])) {
          lonMinStr += data[15];
        }
        lonMin = std::stoi(lonMinStr);
        //setTemperature(latDeg);
        std::cout << "\n lonMin = " << lonMin;


        //we decode each character for the "
        if (isdigit(data[16])) {
          lonSecStr += data[16];
        }
        if (isdigit(data[17])) {
          lonSecStr += data[17];
        }

        lonSecStr += ".";

        if (isdigit(data[18])) {
          lonSecStr += data[18];
        }
        if (isdigit(data[19])) {
          lonSecStr += data[19];
        }
        lonSec = std::stod(lonSecStr);
        //setTemperature(latSec);
        std::cout << "\n lonSec = " << lonSec;


      }
      else
      {
        std::cout << "\nerror: bad data format";
      }
    }

    private :
    double latitude_;
    double longitude_;
  };
}
#endif

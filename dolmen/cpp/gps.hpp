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
      std::cout "work in progress";
      /*int id = getID();
      //latitude
      int latDeg = 0;
      int latMin = 0;
      double latSec = 0.0;
      std::string latstr;


      //latitude


      //longitude


      }
      else
      {
        std::cout << "\nerror: bad data format";
      }*/
    }

    private :
    double latitude_;
    double longitude_;
  };
}
#endif

#include "gps.hpp"

namespace dolmen
{
  Gps::Gps (int id, std::string name):Sensor{id,name}{}

  void Gps::decoding(const std::string data)
  {
    if (data.length() == 21 && data[20] == ';')
    {
      int id = getID();

      //latitude    
      //initialising the values
      //we consider being in the north hemisphere (0-90°N)
      double latDeg = 0.0;
      double latMin = 0.0;
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
      latDeg = std::stod(latDegStr);

      //we decode each character for the '

      if (isdigit(data[4])) {
        latMinStr += data[4];
      }
      if (isdigit(data[5])) {
        latMinStr += data[5];
      }
      latMin = std::stod(latMinStr);

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

      //longitude
      //initialising the values
      double lonDeg = 1.0;
      double lonMin = 0.0;
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
      lonDeg = lonDeg * std::stod(lonDegStr);

      //we decode each character for the '

      if (isdigit(data[14])) {
        lonMinStr += data[14];
      }
      if (isdigit(data[15])) {
        lonMinStr += data[15];
      }
      lonMin = std::stod(lonMinStr);

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

      //inserting datas in the data container
      insert("gps_lonDeg",lonDeg);
      insert("gps_lonMin",lonMin);
      insert("gps_lonSec",lonSec);
      insert("gps_latDeg",latDeg);
      insert("gps_latMin",latMin);
      insert("gps_latSec",latSec);

    }
    else
    {
      //if there is a problem avoiding to decode the data, we insert the value 0.0, and the name become "gps_error_'subdata'"
      std::cout << "\nerror: bad data format";
      insert("gps_error_lonDeg",0.0);
      insert("gps_error_lonMin",0.0);
      insert("gps_error_lonSec",0.0);
      insert("gps_error_latDeg",0.0);
      insert("gps_error_latMin",0.0);
      insert("gps_error_latSec",0.0);
    }
  }

} /* dolmen */

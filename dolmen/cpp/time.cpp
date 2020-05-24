#include "time.hpp"


namespace dolmen
{
  Time::Time (int id, std::string name):Sensor{id,name}{}

  void Time::decoding(const std::string data)
  {
  	//time will be coded in 3 octets hexa caracters, defining the number of seconds since the rocket startup
    double time = 1.0;
    int id = getID();
    if (data.length() == 9 && data[8] == ';')
    {
      time = std::stoi(data, 0, 16);
      insert("time", time);
    }
    else
    {      
      //if an error occurs in the data format, the value is placed at 0
      std::cout << "\nerror: bad data format";
      insert("time_error", 0.0);
    }
  }
} /* dolmen */
#include "time.hpp"


namespace dolmen
{
  Time::Time (int id, std::string name):Sensor{id,name}{}

  void Time::decoding(const std::string data)
  {
    //actual time of the machine
    time_t tmm = time(0);

    //calculating the number of seconds from the launch   
    double time = difftime (tmm, starting);

    insert("time", time);
  }
} /* dolmen */
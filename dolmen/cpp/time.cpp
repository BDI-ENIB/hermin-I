#include "time.hpp"


namespace dolmen
{
  Time::Time (int id, std::string name):Sensor{id,name}{}

  /*void Time::decoding(const std::string data)
  {
    //actual time of the machine
    time_t tmm = time(0);

    //calculating the number of seconds from the launch   
    double time = difftime (tmm, starting);

    insert("time", time);
  }*/

  void Time::decoding(const std::string data)
  {
  	//time will be coded in 2 hexa caracters, defining the number of seconds since the rocket startup
    double time = 1.0;
    std::string data_ = ""; 
    int id = getID();
    if (data.length() == 5 && data[4] == ';')
    {
      //we decode each character
      if (true) {
		data_ += data[2];
      }
      if (true) {
        data_ += data[3];
      }

      time = std::stoi(data_, 0, 16);

      std::cout << "\ntime: " << time << "\n";

      //Temperature::temperature_ = temperature;
      insert("time", time);
    }
    else
    {
      std::cout << "\nerror: bad data format";
      insert("time_error", 0.0);
    }
  }
} /* dolmen */
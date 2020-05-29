
#ifndef DOLMEN_DATE_HPP
#define DOLMEN_DATE_HPP 1

#include <string>

namespace dolmen {

class Date {
private:
  /* data */

public:
  int hour;
  int minute;
  int second;
  int msecond;
  int day;
  int month;
  int year;

  std::string setTime()
  {
    std::string truc;
    return truc;
  }

  Date ();
  virtual ~Date ();
};

} /* dolmen */

#endif

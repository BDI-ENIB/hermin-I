
#ifndef DOLMEN_DATE_HPP
#define DOLMEN_DATE_HPP 1

namespace dolmen {

class Date {
private:
  /* data */

public:
  int hour;
  int minute;
  int second;
  int µsecond;
  int day;
  int month;
  int year;

  string setTime()
  {
    return truc;
  }

  Date (arguments);
  virtual ~Date ();
};

} /* dolmen */

#endif

#ifndef DOLMEN_SENSORS_HPP
#define DOLMEN_SENSORS_HPP 1
#include <string>
#include <iostream>
#include <map>

namespace dolmen
{
  template <class T> class Prototype
  {
  public:
    virtual ~Prototype(){}
    virtual T* Clone() const = 0;
  };

  class Sensor : public Prototype<Sensor>
  {
  public:
      Sensor (int id, std::string name):id{id},name{name}{}

      virtual void decoding(const std::string data) = 0;

      virtual std::map<std::string, double> getValue() = 0;

      virtual std::string getColumnIdentifiers() = 0;

      virtual int getNbAttr() = 0;

      int getID()
      {
        return id;
      }

      std::string getName()
      {
        return name;
      }

    private:
      int id;
      std::string name;
  };
}

#endif

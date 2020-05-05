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
  };

  class Sensor : public Prototype<Sensor>
  {
  public:
      Sensor (int id, std::string name):id{id},name{name}{}

      virtual void decoding(const std::string data) = 0;

      std::map<std::string, double> getValue()
      {
        std::cout << "\n---\n";
        return sensorData;
      }

      void insert(std::string dataName, double dataValue)
      {
        sensorData[dataName] = dataValue;
      }

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
      std::map<std::string, double> sensorData;
  };
}

#endif

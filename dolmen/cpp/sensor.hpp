#ifndef DOLMEN_SENSORS_HPP
#define DOLMEN_SENSORS_HPP 1

#include <string>
#include <iostream>
#include <map>

namespace dolmen
{
  //creating a class prototype
  template <class T> class Prototype
  {
  public:
    virtual ~Prototype() = default;                        //destructeur
  };

  //creating an abstract class (+- interface) for our sensors
  class Sensor : public Prototype<Sensor>
  {
  public:
      Sensor (int id, std::string name):id{id},name{name}{}
      Sensor(const Sensor &) = default;            //constructeur par recopie
      Sensor(Sensor &&) = default;                 //constructeur par déplacement
      Sensor& operator=(const Sensor &) = default; //affectation par recopie
      Sensor& operator=(Sensor &&) = default;      //affectation par déplacement

      virtual void decoding(const std::string data) = 0;

      std::map<std::string, double> getValue()
      {
        return sensorData;
      }

      //to add some datas in the data container
      void insert(std::string dataName, double dataValue)
      {
        sensorData[dataName] = dataValue;
      }

      //[UNUSED]
      //each sensor does have name for each column
      virtual std::string getColumnIdentifiers() = 0;

      //[UNUSED]
      //each sensor does have a known number of columns
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
      //we need a data container, to store the datas read by the sensor
      std::map<std::string, double> sensorData;
  };
}

#endif

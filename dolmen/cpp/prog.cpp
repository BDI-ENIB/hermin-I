#include <vector>
#include <iostream>
#include <memory>
#include <fstream>

#include "dolmen.hpp"

int main(int argc, char const *argv[]) {
  //creating a dolmen element
  dolmen::Dolmen DolMen;

  //reading the datas
  std::ifstream trame("trame.txt");
  std::ofstream ofs{"report.csv"};
  std::string dataTxt;

  //creating a factory element
  using AFactory = dolmen::FactorySensor<std::string, std::unique_ptr<dolmen::Sensor>, int, std::string>;
  AFactory factory;

  //creating a map to store all the sensors
  std::map<int, dolmen::Sensor*> sensorList = std::map<int, dolmen::Sensor*>();

  //---to change to a for---
  //this is a pointer to a sensor element, used to move the sensors from the factory to our map
  dolmen::Sensor* sensor = nullptr;

  //the ksp project uses: 01 temperature / 02 pressure / 03 acceleration/ 04 gps/ 05 altitude/ 06 gyroscope

  //creating a temperature sensor
  factory.registe("temp_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Temperature>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> temperature = factory.create("temp_sensor", 01, "temp");
  sensor = temperature.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  //creating a gyroscope sensor
  factory.registe("gyro_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Gyroscope>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> gyroscope = factory.create("gyro_sensor", 06, "gyro");
  sensor = nullptr;
  sensor = gyroscope.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  //creating an acceleration sensor
  factory.registe("acc_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Acceleration>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> acceleration = factory.create("acc_sensor", 03, "acc");
  sensor = nullptr;
  sensor = acceleration.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  //creating a gps sensor
  factory.registe("gps_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Gps>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> gps = factory.create("gps_sensor", 04, "gps");
  sensor = nullptr;
  sensor = gps.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  //creating a pressure sensor
  factory.registe("pressure_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Pressure>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> pressure = factory.create("pressure_sensor", 02, "pressure");
  sensor = nullptr;
  sensor = pressure.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  //creating an altitude sensor
  factory.registe("altitude_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Altitude>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> altitude = factory.create("altitude_sensor", 05, "altitude");
  sensor = nullptr;
  sensor = altitude.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));

  for (const auto &elem: sensorList)
  {
    std::cout << "je suis une id de sensor " << elem.first << "\n";
  }

  //reading the data trame
  if(trame)
  {
    //each line is a measurement of the rocket, with datas of each sensor
    std::string line;
    while(std::getline(trame,line))
    {
      //extracting data from each line
      std::string data;
      for (auto& letter : line)
      {
        data += letter;
        if (letter == ';')
        {
          std::cout << data << "\n";
          std::cout << "\n";
          std::string dataTxt1 = DolMen.decoding(data, sensorList);
          //std::string dataTxt1 = "jesuisunedonnee";
          std::cout << "\n\n";
          dataTxt += dataTxt1;
          data = "";
        }
        //deleting all the sensors instances
        //temperature->free();
      }
      dataTxt += '\n';
    }
    ofs << dataTxt;
    std::cout << dataTxt;
  }
  else
  {
    std::cout << "unable to open the file";
  }
  return 0;
}

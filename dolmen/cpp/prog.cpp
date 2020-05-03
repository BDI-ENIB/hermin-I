#include <vector>
#include <iostream>
#include <memory>
#include <fstream>

#include "dolmen.hpp"

int main(int argc, char const *argv[]) {

  dolmen::Dolmen DolMen;
  //dolmen::FactorySensor fac;

  //reading the datas
  std::ifstream trame("trame.txt");
  std::ofstream ofs{"report.csv"};
  std::string dataTxt;

  //saving types

  using AFactory = dolmen::FactorySensor<std::string, std::unique_ptr<dolmen::Sensor>, int, std::string>;

  AFactory factory;
  factory.registe("temp_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Temperature>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> temperature = factory.create("temp_sensor", 01, "temp");
  std::cout << "id et nom " << temperature->getID() << " " << temperature->getName() << "\n";
  std::cout << "columnid " << temperature->getColumnIdentifiers() << "\n";
  dolmen::Sensor* sensor = nullptr;
  sensor = temperature.get();


  std::map<int, dolmen::Sensor*> sensorList = std::map<int, dolmen::Sensor*>();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));

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

#include <vector>
#include <iostream>
#include <memory>
#include <fstream>

#include "dolmen.hpp"


int main(int argc, char const *argv[]) {

  dolmen::Dolmen DolMen;

  //reading the datas
  std::ifstream trame("trame.txt");

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
        //sensor list
        std::vector<std::unique_ptr<dolmen::Sensor>> sensorList;
/*
        sensorList.push_back(std::make_unique<dolmen::Temperature> (01, "temp"));
        sensorList.push_back(std::make_unique<dolmen::Pressure> (02, "pres"));
        sensorList.push_back(std::make_unique<dolmen::Acceleration> (03, "acc"));
        sensorList.push_back(std::make_unique<dolmen::Gps> (04, "gps"));
        sensorList.push_back(std::make_unique<dolmen::Altitude> (05, "alt"));
        sensorList.push_back(std::make_unique<dolmen::Gyroscope> (06, "gyr"));*/
        //
        data += letter;
        if (letter == ';')
        {
          /*std::cout << data << "\n";
          std::cout << "\n";
          std::string dataTxt = DolMen.decoding(data, std::move(sensorList));
          std::cout << "\n\n";
          DolMen.exportCsv(dataTxt);
          data = "";*/
        }
      }
      break;
    }
  }
  else
  {
    std::cout << "unable to open the file";
  }
  return 0;
}

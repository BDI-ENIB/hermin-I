#include <vector>
#include <iostream>
#include <memory>

#include "dolmen.hpp"


int main(int argc, char const *argv[]) {

  dolmen::Dolmen DolMen;

  std::string data1 ="01blablabla";
  std::string data2 ="02bliblibli";

  /*std::vector<std::unique_ptr<dolmen::Sensor>> vec;
  vec.push_back(std::unique_ptr<dolmen::Sensor>(new dolmen::Temperature(01, "temp")));
  vec.push_back(std::unique_ptr<dolmen::Sensor>(new dolmen::Pressure(02, "pres")));*/

  std::vector<std::unique_ptr<dolmen::Sensor>> vec;
  vec.push_back(std::unique_ptr<dolmen::Sensor>(std::make_unique<dolmen::Temperature>(01, "temp")));
  vec.push_back(std::unique_ptr<dolmen::Sensor>(std::make_unique<dolmen::Pressure>(02, "pres")));

  for (auto& elem : vec) {
    std::cout << elem->getID() << elem->getName();
  }


  //DolMen.decoding(data1, vec);
  return 0;
}

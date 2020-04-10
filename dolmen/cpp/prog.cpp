#include <vector>
#include <iostream>
#include <memory>

#include "dolmen.hpp"


int main(int argc, char const *argv[]) {

  dolmen::Dolmen DolMen;

  std::string data1 ="01blablabla";
  std::string data2 ="02bliblibli";

  std::cout << data1 << "\n";
  std::cout << data2 << "\n";

  /*std::vector<std::unique_ptr<dolmen::Sensor>> vec;
  vec.push_back(std::unique_ptr<dolmen::Sensor>(std::make_unique<dolmen::Temperature>(01, "temp")));
  vec.push_back(std::unique_ptr<dolmen::Sensor>(std::make_unique<dolmen::Pressure>(02, "pres")));*/

  std::vector<std::unique_ptr<dolmen::Sensor>> vec;
  vec.push_back(std::make_unique<dolmen::Temperature>(01, "temp"));
  vec.push_back(std::make_unique<dolmen::Pressure>(02, "pres"));

  for (auto& elem : vec) {
    std::cout << "\ntest" << "\n";
    std::cout << "id: " << elem->getID() << "\nnom: " << elem->getName();
  }

  std::cout << "\n";
  DolMen.decoding(data1, *vec);
  return 0;
}

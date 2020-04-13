#include <vector>
#include <iostream>
#include <memory>

#include "dolmen.hpp"


int main(int argc, char const *argv[]) {

  dolmen::Dolmen DolMen;

  std::string data1 ="01-3015"; //temperature ou pression
  std::string data2 ="02-4258"; //temperature ou pression

  std::cout << data1 << "\n";
  std::cout << data2 << "\n";

  std::vector<std::unique_ptr<dolmen::Sensor>> vec;
  vec.push_back(std::make_unique<dolmen::Temperature> (01, "temp"));
  vec.push_back(std::make_unique<dolmen::Pressure> (02, "pres"));
  vec.push_back(std::make_unique<dolmen::Acceleration> (03, "acc"));

  for (auto& elem : vec) {
    std::cout << "\ntest" << "\n";
    std::cout << "id: " << elem->getID() << "\nnom: " << elem->getName();
  }

  std::cout << "\n";
  DolMen.decoding(data2, std::move(vec));
  std::cout << "\n\n";
  return 0;
}

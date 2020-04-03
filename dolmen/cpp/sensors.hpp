#ifndef DOLMEN_SENSORS_HPP
#define DOLMEN_SENSORS_HPP 1
#include <string>

namespace dolmen {

class Sensors {
public :
Sensors (int id, std::string name){
    id_=id
    name_=name
}

void decoding();
private :
int id_;
std::string name_;
}

}
#ifndef DOLMEN_Configuration_HPP
#define DOLMEN_Configuration_HPP 1
#include <string>

namespace dolmen {

class Configuration {
public :

bool getWindows_config(){
    return communication_
}

void setWindows_config(bool state){
    communication_= state
}

bool getSensors_config(){
    return communication_
}

void setSensors_config(bool state){
    communication_= state
}


void import_config();
void export_config();

private :
std::string windows_config;
std::string sensors_config;
}

}
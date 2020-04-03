#ifndef DOLMEN_PRESSURE_HPP
#define DOLMEN_PRESSURE_HPP 1
#include <string>
#include"sensors.hpp"
namespace dolmen {

class Pressure : public Sensors{
public :
Pressure (int id, std::string name):
    Sensors{id,name}{}

double getPressure(){
    return pressure_;
}

void setPressure(double newPressure){
    pressure_=newPressure;
}

void decoding() override;
private :
double pressure_;
};

}
#endif
#ifndef DOLMEN_ALTITUDE_HPP
#define DOLMEN_ALTITUDE_HPP 1
#include <string>
#include"sensors.hpp"
namespace dolmen {

class Altitude : public Sensors{
public :
Altitude (int id, std::string name):
    Sensors{id,name}{}

double getAltitude(){
    return altitude_;
}

void setAltitude(double newAltitude){
    altitude_=newAltitude;
}

void decoding() override;
private :
double altitude_;
};

}
#endif
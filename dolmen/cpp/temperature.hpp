#ifndef DOLMEN_TEMPERATURE_HPP
#define DOLMEN_TEMPERATURE_HPP 1
#include <string>
#include"sensors.hpp"
namespace dolmen {

class Temperature : public Sensors{
public :
Temperature (int id, std::string name):
    Sensors{id,name}{}

double getTemperature(){
    return temperature_;
}

void setTemperature(double newTemperature){
    temperature_=newTemperature;
}

void decoding() override;
private :
double temperature_;
};

}
#endif
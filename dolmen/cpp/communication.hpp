#ifndef DOLMEN_Communication_HPP
#define DOLMEN_Communication_HPP 1
#include <string>

namespace dolmen {

class Communication {
public :

bool getCommunication(){
    return communication_
}

void setCommunication(bool state){
    communication_= state
}

bool getFire_mode(){
    return communication_
}

void setFire_mode(bool state){
    communication_= state
}


void frame_receiver();
void frame_import();

private :
bool communication_;
bool fire_mode;
}

}
#ifndef DOLMEN_SENSOR_INIT_HPP
#define DOLMEN_SENSOR_INIT_HPP 1

/*The DolMen user will only need to modify this file if he needs to add new sensors*/

//insert here your sensors hpp files
#include "temperature.hpp"
#include "gyroscope.hpp"
#include "acceleration.hpp"
#include "altitude.hpp"
#include "gps.hpp"
#include "pressure.hpp"

namespace dolmen
{
  //this file is used to create all the new sensors, the user will only need to modify this one
  std::map<int, dolmen::Sensor*> initialise()
  {
    //creating a factory element
    using AFactory = dolmen::FactorySensor<std::string, std::unique_ptr<dolmen::Sensor>, int, std::string>;
    AFactory factory;

    //creating a map to store all the sensors
    std::map<int, dolmen::Sensor*> sensorList = std::map<int, dolmen::Sensor*>();

    //---to change to a for---
    //this is a pointer to a sensor element, used to move the sensors from the factory to our map
    dolmen::Sensor* sensor = nullptr;

    //the ksp project uses: 01 temperature / 02 pressure / 03 acceleration/ 04 gps/ 05 altitude/ 06 gyroscope

    //creating a temperature sensor
    factory.registe("temp_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Temperature>(arg1,arg2); });
    std::unique_ptr<dolmen::Sensor> temperature = factory.create("temp_sensor", 01, "temp");
    sensor = temperature.get();
    sensorList.insert(std::make_pair(sensor->getID(), sensor));
    //creating a gyroscope sensor
    factory.registe("gyro_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Gyroscope>(arg1,arg2); });
    std::unique_ptr<dolmen::Sensor> gyroscope = factory.create("gyro_sensor", 06, "gyro");
    sensor = nullptr;
    sensor = gyroscope.get();
    sensorList.insert(std::make_pair(sensor->getID(), sensor));
    //creating an acceleration sensor
    factory.registe("acc_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Acceleration>(arg1,arg2); });
    std::unique_ptr<dolmen::Sensor> acceleration = factory.create("acc_sensor", 03, "acc");
    sensor = nullptr;
    sensor = acceleration.get();
    sensorList.insert(std::make_pair(sensor->getID(), sensor));
    //creating a gps sensor
    factory.registe("gps_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Gps>(arg1,arg2); });
    std::unique_ptr<dolmen::Sensor> gps = factory.create("gps_sensor", 04, "gps");
    sensor = nullptr;
    sensor = gps.get();
    sensorList.insert(std::make_pair(sensor->getID(), sensor));
    //creating a pressure sensor
    factory.registe("pressure_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Pressure>(arg1,arg2); });
    std::unique_ptr<dolmen::Sensor> pressure = factory.create("pressure_sensor", 02, "pressure");
    sensor = nullptr;
    sensor = pressure.get();
    sensorList.insert(std::make_pair(sensor->getID(), sensor));
    //creating an altitude sensor
    factory.registe("altitude_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Altitude>(arg1,arg2); });
    std::unique_ptr<dolmen::Sensor> altitude = factory.create("altitude_sensor", 05, "altitude");
    sensor = nullptr;
    sensor = altitude.get();
    sensorList.insert(std::make_pair(sensor->getID(), sensor));

    return sensorList;
  }

} /* dolmen */

#endif

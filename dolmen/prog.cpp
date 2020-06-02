#include <vector>
#include <iostream>
#include <memory>
#include <fstream>
#include <time.h>
#include <stdlib.h>

#include "dolmen.hpp"
#include "configuration.hpp"

//---USEFUL THINGS

#include <cstdlib>
#include <unistd.h>

//---MAIN FUNCTION

int main(int argc, char const *argv[]) 
{
  //creating a dolmen element
  dolmen::Dolmen DolMen;
  std::string dataTxt;
  for (int i = 0; i < 5; ++i)
    {
        if(argv[i] != 0)
        {
            std::cout <<"argv "<< i << " = " << argv[i] <<"\n" ;
        }
    }

  //---

  /*
  HOW TO ADD YOUR OWN SENSORS TO THE DOLMEN PROJECT?

  add this code in the list below:

  factory.registe("sensor name", [](int arg1, std::string arg2) { return std::make_unique<dolmen::name of your sensor class>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> sensor name in the map = factory.create("sensor name", sensor id, "sensor name");
  sensor = sensor name in the map.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));

  To remove a sensor, just delete the code corresponding.

  */

  //creating a factory element
  using AFactory = dolmen::FactorySensor<std::string, std::unique_ptr<dolmen::Sensor>, int, std::string>;
  AFactory factory;

  //creating a map to store all the sensors
  std::map<int, dolmen::Sensor*> sensorList = std::map<int, dolmen::Sensor*>();

  //---to change to a for---
  //this is a pointer to a sensor element, used to move the sensors from the factory to our map
  dolmen::Sensor* sensor = nullptr;

  //the ksp project uses: 00 time / 01 gps / 02 accelerometer / 03 gyroscope/ 04 temperature 1/ 05 temperature 2/ 06 pression 1 / 07 pression 2 / 08 altitude

  //creating the clock
  factory.registe("clk", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Time>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> clock = factory.create("clk", 0, "clk");
  sensor = clock.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));


  //creating two temperature sensors
  factory.registe("temp_sensor1", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Temperature>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> temperature1 = factory.create("temp_sensor1", 4, "temp1");
  sensor = temperature1.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));

  factory.registe("temp_sensor2", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Temperature>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> temperature2 = factory.create("temp_sensor2", 5, "temp2");
  sensor = temperature2.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  
  //creating a gyroscope sensor
  factory.registe("gyro_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Gyroscope>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> gyroscope = factory.create("gyro_sensor", 3, "gyro");
  sensor = nullptr;
  sensor = gyroscope.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  
  //creating an acceleration sensor
  factory.registe("acc_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Acceleration>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> acceleration = factory.create("acc_sensor", 2, "acc");
  sensor = nullptr;
  sensor = acceleration.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  
  //creating a gps sensor
  factory.registe("gps_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Gps>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> gps = factory.create("gps_sensor", 1, "gps");
  sensor = nullptr;
  sensor = gps.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  
  //creating two pressure sensors
  factory.registe("pressure_sensor1", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Pressure>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> pressure1 = factory.create("pressure_sensor1", 6, "pressure1");
  sensor = nullptr;
  sensor = pressure1.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));

  factory.registe("pressure_sensor2", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Pressure>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> pressure2 = factory.create("pressure_sensor2", 7, "pressure2");
  sensor = nullptr;
  sensor = pressure2.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));
  
  //creating an altitude sensor
  factory.registe("altitude_sensor", [](int arg1, std::string arg2) { return std::make_unique<dolmen::Altitude>(arg1,arg2); });
  std::unique_ptr<dolmen::Sensor> altitude = factory.create("altitude_sensor", 8, "altitude");
  sensor = nullptr;
  sensor = altitude.get();
  sensorList.insert(std::make_pair(sensor->getID(), sensor));

  //---
  //checking if we are allowed to decode
  std::ofstream ofs{argv[2]};
  ofs.close();
  std::ofstream initConfig(argv[1]);
  initConfig<<"false";
  initConfig.close();
  while(1)
  {
    //importing the configuration
    std::map<std::string, std::string> configuration = dolmen::import_config(argv[1]);
    //std::ifstream trame(configuration["data_path"]);
    usleep(1000000);
    if (configuration["decoding_authorised"] == "true")
    {
      
      //using offline mode
      if (configuration["mode"] == "offline")
      {
        std::ifstream trame(configuration["data_path"]);
        //reading the data trame
        if(trame)
        {
          std::cout << "\n---Launching DolMen in offline mode---\n";
          //each line is a measurement of the rocket, with datas of each sensor
          std::string line;
          //allow to select another name for the datas
          std::ofstream ofs{argv[2]};
          while(std::getline(trame,line))
          {
            //---
            time_t seconds;
            struct tm instant;
            time(&seconds);
            instant=*localtime(&seconds);
            printf("\n\n%d/%d ; %d:%d:%d", instant.tm_mday+1, instant.tm_mon+1, instant.tm_hour, instant.tm_min, instant.tm_sec);
            //this is the time in 10-6 seconds to wait until each read
            usleep(100);
            //---

            //extracting data from each line
            //dataTxtLine is used to detect the empty lines
            std::string dataTxtLine;
            //data contain the unprocessed datas from one sensor
            std::string data;
            for (auto& letter : line)
            {
              data += letter;
              //detecting a sensor, which is separated from other sensors by a ';' tag
              if (letter == ';')
              {
                //adding the processed datas
                dataTxtLine += DolMen.decoding(data, sensorList);
                data = "";
              }
            }
            //if no data was processed (empty line), we don't add a \n caracter
            dataTxt += dataTxtLine;
            if (dataTxtLine != "")
            {
              dataTxt += '\n';
            }
            dataTxtLine = "";
          }
          //writing the datas in the .csv file
          dataTxt += "stop\n";
          ofs << dataTxt;          
          dataTxt="";
          std::ofstream resetConfig(argv[1]);
          resetConfig<<"false";
          resetConfig.close();
          std::cout << "\n\n---Closing---\n";
        }
        else 
        {
          //error to add later
          std::cout << "\nUnable to open the file";
        }
        std::cout << "\n";
      }
      if (configuration["mode"] == "online")
      {
        //ONLINE MODE IS NOT TESTED, PLEASE CONSIDER THIS AS A NON WORKING MODE
        //reading the data trame
        std::ifstream trame(configuration["data_path"]);
        if(trame)
        {
          std::cout << "\n---Launching DolMen in online mode---\n";
          //each line is a measurement of the rocket, with datas of each sensor
          std::string line;
          
          while(std::getline(trame,line) && configuration["decoding_authorised"] == "true")
          {
            std::ofstream ofs{argv[2],std::ios::app};
            //---
            time_t seconds;
            struct tm instant;
            time(&seconds);
            instant=*localtime(&seconds);
            printf("\n\n%d/%d ; %d:%d:%d", instant.tm_mday+1, instant.tm_mon+1, instant.tm_hour, instant.tm_min, instant.tm_sec);
            //this is the time in 10-6 seconds to wait until each read
            //we set here with the time between 2 emissions from our rocket
            usleep(1000000);
            //---

            //extracting data from each line
            //dataTxtLine is used to detect the empty lines
            std::string dataTxtLine;
            //data contain the unprocessed datas from one sensor
            std::string data;
            for (auto& letter : line)
            {
              data += letter;
              //detecting a sensor, which is separated from other sensors by a ';' tag
              if (letter == ';')
              {
                //adding the processed datas
                dataTxtLine += DolMen.decoding(data, sensorList);
                data = "";
              }
            }
            //writing the datas in the .csv file
            std::cout << "\nline decoded" << dataTxtLine;
            ofs << dataTxtLine;
            ofs << '\n';
            ofs.close();
            std::cout << "\n\n---Closing---\n";
            //resetting the line
            dataTxtLine = "";
            //checking is we're still allowed to decode
            configuration = dolmen::import_config(argv[1]);
          }
          std::ofstream resetConfig(argv[1]);
          resetConfig<<"false";
          resetConfig.close();
        }
      }
    }
    else
    {
      //Error to add
      //std::cout << "\nDecoding not allowed";
      if (configuration["decoding_authorised"] == "exit")
      {
        exit(0);
      }
    }
  }
  std::cout << "\n\n---Closing---\n";
  return 0;
}

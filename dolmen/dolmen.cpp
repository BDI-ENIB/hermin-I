#include "dolmen.hpp"

#include <cmath>

namespace dolmen
{
  Dolmen::Dolmen(){}

  //std::string Dolmen::decoding(std::string data, std::map<int, std::unique_ptr<dolmen::Sensor>> sensors_list);
  std::string Dolmen::decoding(std::string data, std::map<int, dolmen::Sensor*> sensorList)
  {
    //reading the sensor id from the data frame
    std::string idstr;
    if (isdigit(data[0]))
    {
      idstr += data[0];
    }
    if (isdigit(data[1]))
    {
      idstr += data[1];
    }

    //converting the sensor id into an int
    int id = std::stoi(idstr);

    //finding the correct sensor in the sensor list by matching the id with the data frame id
    //dolmen::Sensor* elem;
    dolmen::Sensor* elem;
    if (auto it = sensorList.find(id); it != sensorList.end())
    {
      elem = it->second;
    }

    //searching the maximum number of datas returned by the sensor
    //(some sensors can return one value, some can return many values)
    int max = 0;
    if (elem->getID() == id)
    {
      //decoding the data with the correct sensor, to create a map which contain all the datas of the sensor, from our data frame
      elem->decoding(data);

      if(abs(int(elem->getValue().size())/elem->getNbAttr()) > max)
      {
        max = int(elem->getValue().size());
      }
    }
    else
    {
      std::cout << "\nsensor not found\n";
    }

    //recovering values, and writing the csv file

    //this string is the return value of the function
    std::string dataTxt;
    //this string is the value of the sensors data in the csv file
    std::string columnValueTxt;

    bool found = false;

    if (elem->getID() == id)
    {
      //writing the data identifier
      //columnValueTxt += elem->getColumnIdentifiers();
      //columnValueTxt += elem->getName();
      //columnValueTxt += ";";
      columnValueTxt += std::to_string(elem->getID());
      columnValueTxt += ";";
      //recovering the processed data from the sensor
      std::map<std::string, double> processed_data = elem->getValue();

      //writing each element of the processed data
      int i = 0;
      for (std::pair<std::string, double> elem2 : processed_data)
      {
        //writing the data
        columnValueTxt+= std::get<0>(elem2);
        columnValueTxt+= ";";
        columnValueTxt+= std::to_string(std::get<1>(elem2));
        columnValueTxt+= ";";
        //this prevents to write a longer line than the number of datas
        if(i >= elem->getNbAttr()-1)
        {
          break;
        }
        i+=1;
      }
      //adding a blank case between each sensor
      columnValueTxt+= ";";
      //adding the sensors datas to the .csv
      dataTxt+=columnValueTxt;
    }
    else
    {
      dataTxt = "error: Dolmen::decoding() failed ,";
    }
    //we return the string matching our data frame we will write in our csv file
    //std::cout << "\n\n dataTxt: " << dataTxt << "\n\n";
    return dataTxt;
  }
} /* dolmen */

#include "dolmen.hpp"

#include <cmath>

namespace dolmen
{
  Dolmen::Dolmen(){}

  std::string Dolmen::decoding(std::string data, std::map<int, std::unique_ptr<dolmen::Sensor>> sensors_list);
  {
    //reading the sensor id
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

    std::string dataTxt;

    //premiere partie on decode et on recupere le nombre de lignes max
    int max = 0;
    for (const auto& elem : sensors_list)
    {
      if (elem->getID() == id)
      {
        elem->decoding(data);

        if(abs(int(elem->getValue().size())/elem->getNbAttr()) > max)
        {
          max = int(elem->getValue().size());
        }
        break;
      }
      else
      {
        std::cout << "\nsensor not found\n";
      }
    }
    //seconde partie on recupere les valeurs et on les formatte en csv
    std::string columnValueTxt;
    std::string columnsTxt;
    bool found = false;
    for (const auto& elem : sensors_list)
    {
      if (elem->getID() == id)
      {
        columnValueTxt += elem->getColumnIdentifiers();
        columnValueTxt += ";";
        std::map<std::string, double> processed_data = elem->getValue();
        int i = 0;
        for (const auto &elem2 : processed_data)
        {
          columnValueTxt+= std::to_string(std::get<1>(elem2));
          if(i < elem->getNbAttr())
          {
            columnValueTxt+= ";";
          }
          else
          {
            columnValueTxt+= "\n";
          }
          i++;
          found = true;
          break;
        }
        //completer les lignes avec le max
        i=0;
        for (int j=0; j<max;j++)
        {
          if(i < elem->getNbAttr())
          {
            columnValueTxt+= ";";
          }
          else
          {
            columnValueTxt+= "\n";
          }
          i++;
        }
        dataTxt+=columnValueTxt;
        if (found == false)
        {
          //error to add
          std::cout<<"\n ---error: unknown sensor--- \n";
        }
        break;
      }
      else
      {
        dataTxt = "error: Dolmen::decoding() failed";
      }
    }
    return dataTxt;
  }
} /* dolmen */

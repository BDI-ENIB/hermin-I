#include "dolmen.hpp"

namespace dolmen
{
  Dolmen::Dolmen(){}

  std::string Dolmen::decoding(std::string data, std::vector<std::unique_ptr<dolmen::Sensor>> sensors_list)
  {
    //reading data to determine the sensor
    std::cout << "\n j'entre dans dolmen::decoding \n";

    //reading the sensor id
    std::string idstr;
    if (isdigit(data[0])) {
      idstr += data[0];
    }
    if (isdigit(data[1])) {
      idstr += data[1];
    }

    //converting the sensor id into an int
    int id = std::stoi(idstr);

    //std::cout << "\n id chaine = " << idstr << "\n";
    //std::cout << "\n id int = " << id << "\n";

    std::string dataTxt;
    /*
    bool found = false;
    for (const auto& elem : sensors_list)
    {
    //std::cout << elem->getID() << "=" << id << "?\n";
    if (elem->getID() == id)
    {
    elem->decoding(data);
    std::map<std::string, double> processed_data = elem->getValue();
    dataTxt += elem->getName();
    dataTxt += ",";
    dataTxt += " ";
    dataTxt += ",";
    found = true;
    std::cout << "\nsensor found: " << id;
    break;
  }
}*/
//premiere partie on decode et on recupere le nombre de lignes max
*--premiere partie on decode et on recupere le nombre de lignes max*
int max = 0;
for (const auto& elem : sensors_list)
{
  //std::cout << elem->getID() << "=" << id << "?\n";
  if (elem->getID() == id)
  {
    elem->decoding(data);

    if(elm=>getValue().size()/getNbAttr() > max){
      max=elm=>getValue().size();
    }
  }
}
*-- seconde partie on recupere les valeurs et on les formatte en csv*
std::string columnValueTxt;
bool found = false;
for (const auto& elem : sensors_list)
{
  //std::cout << elem->getID() << "=" << id << "?\n";
  if (elem->getID() == id)
  {
    columnsTxt += elem->getcolumnIden....
    columnsTxt += ";";
    std::map<std::string, double> processed_data = elem->getValue...
    int i =0;
    for (const auto &dat : data) {
      columnValueTxt+= std::to_string(element.second);
      if(i < elem->getNbAttr()){
        columnValueTxt+= ";";
      }else {
        columnValueTxt+= "\n";
      }
      i++;
      found = true;
      std::cout << "\nsensor found: " << id;
    }
    //completer les lignes avec le max
    i=0;
    for (int j=0; j<max;j++) {
      if(i < elem->getNbAttr()){
        columnValueTxt+= ";";
      }else {
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

    return dataTxt;
  }
} /* dolmen */

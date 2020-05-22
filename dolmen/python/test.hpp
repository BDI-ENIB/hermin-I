#ifndef DOLMEN_TEST_HPP
#define DOLMEN_TEST_HPP 1
#include <string>
namespace dolmen
{

   class Test
  {
    public :
      Test (int id, std::string name)
      {
        int id_=id;
        std::string name_=name;
        int a_=a;
      }


      virtual ~Test() 
      {
        //
      }

      virtual void decoding(const std::string data) = 0;

      int getID()
      {
        return id_;
      }

      int getA()
      {
        return a_;
      }
    private :
      int id_;
      std::string name_
      int a_;
  };
}

#endif

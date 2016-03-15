#include <iostream>
#include <cstdlib>

#define MAX_INT 100000;

struct eano{
  int index,su,pr;
  float possibility;
};

struct queue{
  int head,tail;
  eano data[MAX_INT];
};

queue q1,q2;


using namespace std;

int main()
{
  q1.data[q1.tail].index=10;
  cout<<q1.data[q1.tail].index;
  return 0;
}

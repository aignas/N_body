// Written by Ignas Anikevicius in 2012
// 
// Should compile with g++
//
// Do whatever you want with the code.

#include <iostream>

using namespace std;

double Force ( double& G,
               double& M,
               double& m,
               double r );

int main (void)
{
    cout << "This program will calculate the Newtonian Force"
         << endl;

    double G = 1.0,
           M = 5, 
           m = 1;
    double r = .5;

    cout << "The value of G used in the calculations will be "
         << G
         << endl;

    double force = Force(G,M,m,r);

    cout << "The force is " << force << endl;

    return 0;
}

double Force ( double& G,
               double& M,
               double& m,
               double r )
{
    return G*m*M/(r*r);
}

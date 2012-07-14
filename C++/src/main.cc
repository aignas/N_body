// Written by Ignas Anikevicius in 2012
// 
// Should compile with g++
//
// Do whatever you want with the code.

#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<double>
Force( const double& G,
        const double& M,
        const double& m,
        vector<double>& r );

double
modulus_vector( vector<double> r );

int
func ( double t, const double y[], double f[], void *params )
{
    double GM = *(double *) params;
    f[0] = y[1];
    f[1] = -y[0];
    return GSL_SUCCESS;
}

int
main( void )
{
    const double G = 1, 
          M = 500,
          m = 1, 
          dt = 5e-3;
    unsigned int dimensions = 2;

    bool CONTINUE = true;

    // initiate the position and velocity vectors:
    vector<double> r;
    r.resize(dimensions);
    vector<double> v = r;

    // Set the initial components
    v[0] = 0 ; r[0] = 5;
    v[1] = 10; r[1] = 0;

    cout << "x,y," << endl;
    int I = 0;
    while (CONTINUE)
    {
        vector<double> F = Force (G,M,m,r);
        for ( int i = 0; i < r.size(); ++i )
        {
            r[i] += v[i]*dt;
            v[i] += F[i]*dt/m;
        }

        if ( I % 10 == 0 )
        {
            for ( int i = 0; i < r.size(); ++i )
            {
                cout << r[i] << ",";
            }
            cout << endl;
        }
        I += 1;
    }

    return 0;
}

// This function calculates the vector of a gravitational force
vector<double>
Force( const double& G,
        const double& M,
        const double& m,
        vector<double>& r )
{
    // Calculate the modulus of the vector
    double mod_r = modulus_vector(r);
    // Allocate a vector, which will be later returned.
    vector<double> F;

    // Calculate each vector component separately
    for (int i = 0; i < r.size(); ++i)
    {
        // Note the minus sign
        F.push_back( -G*m*M/(mod_r*mod_r*mod_r)*r[i]);
    }

    return F;
}

// This function calculates the modulus of a vector
double
modulus_vector( vector<double> r )
{
    double modulus_squared = 0;
    for (int i = 0; i < r.size(); ++i)
    {
        modulus_squared += r[i]*r[i];
    }

    return sqrt(modulus_squared);
}

// vim: tw=72

#include<fstream>
#include<cmath>
#include<string>
#define N 33


struct Error_Point
{
    double V;
    double e_V;
    double I;
    double e_I;

    Error_Point(){}
    friend std::istream& operator>>(std::istream& is, Error_Point& p)
    {
        is>>p.V>>p.e_V>>p.I/*>>p.e_I*/;
	return is;
    }
};

struct Error_Point_Array
{
    Error_Point el[N];
    Error_Point_Array(){}

    double fit_value(std::string scale)
    {

    }


    friend std::istream& operator>>(std::istream& is, Error_Point_Array& arr)
    {
        for(int i=0;i<N;i++)
	{
	    is>>arr.el[i];
	}
	return is;
    }
    friend std::ostream& operator<<(std::ostream& os, Error_Point_Array& arr)
    {
        os<<"V = [";
	for(int i=0;i<N;i++)
	{
	    os<<arr.el[i].V;
	    if( i < N-1)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"e_V = [";
	for(int i=0;i<N;i++)
	{
	    os<<arr.el[i].e_V;
	    if( i < N-1)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"I = [";
	for(int i=0;i<N;i++)
	{
	    os<<arr.el[i].I;
	    if( i < N-1)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

/*        os<<"e_I = [";
	for(int i=0;i<N;i++)
	{
	    os<<arr.el[i].e_I;
	    if( i < N-1)
	        os<<", ";
	    else
	        os<<"]";
	}
*/	os<<"\n";
    }
};



int main() 
{
   std::ifstream input;
   input.open("dati.txt");
   Error_Point_Array pydata;
   input>>pydata;
   input.close();

   std::ofstream output;
   output.open("dati.py");
   output<<pydata;
   output.close();
   
}



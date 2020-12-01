#include<fstream>
#include<cmath>
#include<string>

struct Error_Point
{
    double V;
    double e_V;
    double I;
    double e_I;

    Error_Point(){}
    friend std::istream& operator>>(std::istream& is, Error_Point& p)
    {
        is>>p.V>>p.e_V>>p.I>>p.e_I;
	return is;
    }
};

struct Error_Point_Array
{
    Error_Point el[25];
    Error_Point_Array(){}

    double fit_value(std::string scale)
    {

    }


    friend std::istream& operator>>(std::istream& is, Error_Point_Array& arr)
    {
        for(int i=0;i<25;i++)
	{
	    is>>arr.el[i];
	}
	return is;
    }
    friend std::ostream& operator<<(std::ostream& os, Error_Point_Array& arr)
    {
        os<<"V = [";
	for(int i=0;i<25;i++)
	{
	    os<<arr.el[i].V;
	    if( i < 24)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"e_V = [";
	for(int i=0;i<25;i++)
	{
	    os<<arr.el[i].e_V;
	    if( i < 24)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"I = [";
	for(int i=0;i<25;i++)
	{
	    os<<arr.el[i].I;
	    if( i < 24)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"e_I = [";
	for(int i=0;i<25;i++)
	{
	    os<<arr.el[i].e_I;
	    if( i < 24)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";
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



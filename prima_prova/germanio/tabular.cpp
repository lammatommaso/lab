#include<fstream>
#include<cmath>
#include<string>

#define N 15

const std::string nl = "\\";
const std::string NL = nl + nl;

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
	friend std::ostream& operator<<(std::ostream& os, Error_Point& p)
    {
        os<<p.V<<" & "<<sqrt(p.e_V*p.e_I+ 0.03*p.V*0.03*p.V)<<" & "<<p.I<<" & "<<p.e_I<<NL;;
	return os;
    }
};

struct Error_Point_Array
{
    Error_Point el[N];
    Error_Point_Array(){}

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
		for(int i=0;i<N;i++)
		{
			os<<arr.el[i]<<'\n';
		}
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
   output.open("tabular.tex");
   output<<pydata;
   output.close();
}



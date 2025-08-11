#include <iostream>
#include <cmath>

int main(int argc, char** argv){
	int b,ex,i,result;
	char n='s';
	while(n=='s'){
		i=0;
	std::cout <<"Digite a base: ";
	std::cin >>b;
	
	std::cout <<"Digite o expoente: ";
	std::cin >>ex;
	
	result = pow(b,ex);
	
	while(i < ex){
		std::cout << b;
		if(i < ex-1){
			std::cout <<"x";
		}
		i++;
	}
	std::cout<< "=" <<result;
	
	std::cout<< "\nUsar novamente (s/n)?"
	;std::cin >>n;
	}
	return 0;
}




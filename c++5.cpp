#include <iostream>
#include <string>

int main() {
    std::string palavra;
    std::cout << "Digite uma palavra: ";
    std::cin >> palavra;

    int inicio = 0;
    int fim = palavra.length() - 1;
    bool ehpalindromo = true;

    while (inicio < fim) {
        if (palavra[inicio] != palavra[fim]) {
            ehpalindromo = false;
            break;
        }
        inicio++;
        fim--;
    }

    if (ehpalindromo) {
        std::cout << palavra << " e um palindromo.";
    } else {
        std::cout << palavra << " nao e um palindromo.";
       
    }
    

    return 0;
}

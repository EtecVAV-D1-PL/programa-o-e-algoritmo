#include <iostream>
#include <string>

int main() {
    double alt, pi;
    std::string sx;
    char n = 's';

    while (n == 's') {
        std::cout << "Qual o seu sexo (homem/mulher): ";
        std::cin >> sx;

        std::cout << "Qual a sua altura: ";
        std::cin >> alt;

        if (sx == "homem" || sx == "Homem" || sx == "HOMEM") {
            pi = 72.7 * alt - 58;
            std::cout << "Seu peso ideal e " << pi;
        } else if (sx == "mulher" || sx == "Mulher" || sx == "MULHER") {
            pi = 62.1 * alt - 44.7;
            std::cout << "Seu peso ideal e " << pi;
        } else {
            std::cout << "Sexo invalido";
        }

        std::cout << "Usar novamente (s/n)? ";
        std::cin >> n;
    }

    return 0;
}

#include <iostream>
#define PI 3.14

double area(double raio) {
    return PI * raio * raio;
}

int main() {
    double num[5];
    char r = 's';

    while (r == 's' || r == 'S') {
        for (int i = 0; i < 5; i++) {
            std::cout << "Digite o raio do " << i + 1 << "º circulo: ";
            std::cin >> num[i];
        }

        for (int i = 0; i < 5; i++) {
            std::cout << "Area do " << i + 1 << "º circulo: " 
                      << area(num[i]) << "\n";
        }

        std::cout << "Usar novamente? (s/n): ";
        std::cin >> r;
    }

    return 0;
}


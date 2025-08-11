#include <iostream>

void substituirVogais(char palavra[]) {
    int i = 0;
    while (palavra[i] != '\0') {
        char c = palavra[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            palavra[i] = '*';
        }
        i++;
    }
}

int main() {
    char palavra[108];
    char n = 's';

    while (n == 's' || n == 'S') {
        std::cout << "Digite uma palavra ou frase: ";
        std::cin.ignore();
        std::cin.getline(palavra, 108);

        substituirVogais(palavra);

        std::cout << "Palavra modificada: " << palavra << std::endl;

        std::cout << "Usar novamente? (s/n): ";
        std::cin >> n;
    }

    return 0;
}


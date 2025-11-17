# QUIZ ARDUINO
# GRUPO: Laura Duarte Arruda dos Santos, Lucas Oliveira, Nicolas Batista Sarraiva,
# Pedro Coraine, Pedro Henrique Nascimento Rodrigues

import random  # Biblioteca usada para sortear perguntas e embaralhar alternativas

# Mensagem inicial
def mensagem_inicial():
    print("\x1b[1mSeja bem-vindo ao Quiz de Arduino!\x1b[0m\n")

# Regras do jogo
def mostrar_regras():
    print("\n REGRAS DO QUIZ ")
    print("1. O quiz possui 50 perguntas no banco.")
    print("2. Serão sorteadas 20 perguntas por execução.")
    print("3. Cada questão vale 0,5 ponto (nota máxima = 10).\n")

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

# Banco de perguntas (50 perguntas humanizadas)
def criar_banco():
    return [

        # 1
        {"pergunta": "Qual desses é um dos criadores do  Arduino?",
         "alternativas": ["Bill Gates", "Steve Wozniak", "Linus Torvalds", "Mark Zuckerberg", "Massimo Banzi"],
         "correta": "A palavra 'Oi' com quebra de linha"},

        # 2
        {"pergunta": "O pino A0 do Arduino UNO serve para ler que tipo de sinal?",
         "alternativas": ["PWM", "Analógico", "Digital", "USB", "Serial"],
         "correta": "Analógico"},

        # 3
        {"pergunta": "Qual programa é usado para escrever e enviar códigos ao Arduino?",
         "alternativas": ["Arduino IDE", "Photoshop", "Excel", "Eclipse", "Unity"],
         "correta": "Arduino IDE"},

        # 4
        {"pergunta": "Para controlar um motor DC sem danificar o Arduino, é recomendado usar:",
         "alternativas": ["Transistor ou relé", "Apenas resistor", "LDR", "LED", "Capacitor"],
         "correta": "Transistor ou relé"},

        # 5
        {"pergunta": "O comando analogWrite(9, 128) gera:",
         "alternativas": ["PWM com 50% do ciclo ativo", "Sinal HIGH", "Sinal LOW", "Sinal analógico real", "Um erro no Arduino"],
         "correta": "PWM com 50% do ciclo ativo"},

        # 6
        {"pergunta": "A porta USB do Arduino serve principalmente para:",
         "alternativas": ["Transferir dados e energia", "Ligar motores", "Ler sensores", "Aumentar voltagem", "Fazer comunicação Bluetooth"],
         "correta": "Transferir dados e energia"},

        # 7
        {"pergunta": "O LED integrado da placa Arduino UNO está no pino:",
         "alternativas": ["2", "7", "9", "13", "A0"],
         "correta": "13"},

        # 8
        {"pergunta": "Uma variável do tipo int serve para armazenar:",
         "alternativas": ["Texto", "Número inteiro", "Número decimal", "Estado lógico", "Comandos"],
         "correta": "Número inteiro"},

        # 9
        {"pergunta": "A tensão de operação do Arduino UNO é:",
         "alternativas": ["3,3V", "5V", "7V", "9V", "12V"],
         "correta": "5V"},

        # 10
        {"pergunta": "digitalWrite(13, HIGH) faz:",
         "alternativas": ["Liga o pino 13", "Desliga o pino 13", "Pisca o LED", "Reinicia o Arduino", "Nada"],
         "correta": "Liga o pino 13"},

        # 11
        {"pergunta": "O termo PWM significa:",
         "alternativas": ["Pulse Width Modulation", "Power Wave Mode", "Port Width Meter", "Pulse Water Motion", "Power With Motor"],
         "correta": "Pulse Width Modulation"},

        # 12
        {"pergunta": "O Arduino pode ser descrito como:",
         "alternativas": ["Um microcontrolador programável", "Um sensor", "Um motor", "Um sistema operacional", "Um amplificador"],
         "correta": "Um microcontrolador programável"},

        # 13
        {"pergunta": "O comando delay(1000) faz o programa esperar:",
         "alternativas": ["1 segundo", "100 segundos", "1 ms", "10 segundos", "Não faz esperar"],
         "correta": "1 segundo"},

        # 14
        {"pergunta": "Para ler um pino digital usamos:",
         "alternativas": ["digitalRead()", "analogRead()", "readPin()", "pinMode()", "readSerial()"],
         "correta": "digitalRead()"},

        # 15
        {"pergunta": "A função millis() retorna:",
         "alternativas": ["O tempo em ms desde que o Arduino ligou", "A voltagem do pino", "A temperatura", "O valor lido no A0", "A memória usada"],
         "correta": "O tempo em ms desde que o Arduino ligou"},

        # 16
        {"pergunta": "Serial.begin(9600) serve para:",
         "alternativas": ["Iniciar comunicação serial", "Aumentar tensão", "Ligar LED", "Criar variáveis", "Ativar Wi-Fi"],
         "correta": "Iniciar comunicação serial"},

        # 17
        {"pergunta": "Os pinos de PWM são marcados com:",
         "alternativas": ["~", "*", "+", "-", "/"],
         "correta": "~"},

        # 18
        {"pergunta": "O sensor que mede temperatura e umidade é o:",
         "alternativas": ["DHT11", "LDR", "PIR", "HC-SR04", "MQ-2"],
         "correta": "DHT11"},

        # 19
        {"pergunta": "O sensor LDR mede:",
         "alternativas": ["Luz", "Som", "Gás", "Distância", "Vibração"],
         "correta": "Luz"},

        # 20
        {"pergunta": "Um if() serve para:",
         "alternativas": ["Verificar condições", "Repetir código", "Criar funções", "Ler sensores", "Enviar dados"],
         "correta": "Verificar condições"},

        # 21
        {"pergunta": "Um 'sketch' é:",
         "alternativas": ["Um programa do Arduino", "Um sensor", "Um motor", "Um erro de sintaxe", "Um tipo de resistor"],
         "correta": "Um programa do Arduino"},

        # 22
        {"pergunta": "A extensão dos arquivos da Arduino IDE é:",
         "alternativas": [".ino", ".exe", ".txt", ".cpp", ".bin"],
         "correta": ".ino"},

        # 23
        {"pergunta": "O sensor PIR é usado para detectar:",
         "alternativas": ["Movimento", "Luz", "Gás", "Temperatura", "Umidade"],
         "correta": "Movimento"},

        # 24
        {"pergunta": "Uma biblioteca no Arduino é:",
         "alternativas": ["Conjunto de funções prontas", "Um sensor", "Um motor", "Uma IDE", "Um código aleatório"],
         "correta": "Conjunto de funções prontas"},

        # 25
        {"pergunta": "INPUT_PULLUP ativa:",
         "alternativas": ["Resistor interno de pull-up", "PWM", "Bluetooth", "EEPROM", "ADC"],
         "correta": "Resistor interno de pull-up"},

    ]
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

        # 26
        {"pergunta": "tone(8, 1000) faz:",
         "alternativas": ["Gerar som de 1kHz no pino 8", "Ler sensor", "Ligar motor", "Apagar LED", "Criar variável"],
         "correta": "Gerar som de 1kHz no pino 8"},

        # 27
        {"pergunta": "O Arduino UNO tem quantos pinos analógicos?",
         "alternativas": ["6", "8", "4", "10", "12"],
         "correta": "6"},

        # 28
        {"pergunta": "map(x, 0, 1023, 0, 255) faz:",
         "alternativas": ["Converte uma faixa de valores", "Liga motor", "Pisca LED", "Lê sensor", "Reinicia o Arduino"],
         "correta": "Converte uma faixa de valores"},

        # 29
        {"pergunta": "O componente que transforma energia elétrica em movimento é:",
         "alternativas": ["Motor", "LED", "Resistor", "Sensor", "Capacitor"],
         "correta": "Motor"},

        # 30
        {"pergunta": "HIGH e LOW representam:",
         "alternativas": ["Níveis de tensão", "Temperatura", "Vibração", "Velocidade", "Distância"],
         "correta": "Níveis de tensão"},

        # 31
        {"pergunta": "O chip principal do Arduino UNO é o:",
         "alternativas": ["ATmega328P", "RX580", "ESP32", "ARM Cortex", "ATtiny85"],
         "correta": "ATmega328P"},

        # 32
        {"pergunta": "A estrutura for() é usada para:",
         "alternativas": ["Repetição de código", "Criar funções", "Ler sensores", "Enviar dados", "Aumentar tensão"],
         "correta": "Repetição de código"},

        # 33
        {"pergunta": "O resistor em série com um LED serve para:",
         "alternativas": ["Evitar queimar o LED", "Aumentar brilho", "Criar PWM", "Gerar som", "Medir temperatura"],
         "correta": "Evitar queimar o LED"},

        # 34
        {"pergunta": "Para controlar um servo motor usamos:",
         "alternativas": ["PWM", "Analógico", "EEPROM", "USB", "Bluetooth"],
         "correta": "PWM"},

        # 35
        {"pergunta": "O módulo Bluetooth mais comum é o:",
         "alternativas": ["HC-05", "LDR", "DHT11", "MQ-2", "BMP180"],
         "correta": "HC-05"},

        # 36
        {"pergunta": "analogRead(A0) retorna valores entre:",
         "alternativas": ["0 e 1023", "0 e 255", "1 e 10", "0 e 5", "10 e 100"],
         "correta": "0 e 1023"},

        # 37
        {"pergunta": "A memória EEPROM serve para:",
         "alternativas": ["Guardar dados permanentemente", "Ler sensores", "Criar PWM", "Aumentar tensão", "Reiniciar o Arduino"],
         "correta": "Guardar dados permanentemente"},

        # 38
        {"pergunta": "IDE significa:",
         "alternativas": ["Integrated Development Environment", "Internal Device Emulator", "Interface Digital Externa", "Input Device Editor", "In-Dual Engine"],
         "correta": "Integrated Development Environment"},

        # 39
        {"pergunta": "A linguagem principal do Arduino é:",
         "alternativas": ["C/C++", "Python", "Java", "HTML", "Go"],
         "correta": "C/C++"},

        # 40
        {"pergunta": "while(true) faz o programa:",
         "alternativas": ["Repetir para sempre", "Apagar variáveis", "Travarse", "Ler sensores", "Criar PWM"],
         "correta": "Repetir para sempre"},

        # 41
        {"pergunta": "O pino VIN é usado para:",
         "alternativas": ["Alimentar com fonte externa", "Enviar dados", "Ligar motor", "Resetar Arduino", "Ler sensores"],
         "correta": "Alimentar com fonte externa"},

        # 42
        {"pergunta": "O sensor MQ-2 detecta:",
         "alternativas": ["Gases inflamáveis", "Luz", "Som", "Distância", "Vibração"],
         "correta": "Gases inflamáveis"},

        # 43
        {"pergunta": "Capacitores servem para:",
         "alternativas": ["Armazenar carga temporária", "Gerar luz", "Ler sensores", "Criar código", "Converter dados"],
         "correta": "Armazenar carga temporária"},

        # 44
        {"pergunta": "Ligar um LED diretamente no 5V causa:",
         "alternativas": ["Queima do LED", "LED mais forte", "Nada", "Erro no código", "Reboot"],
         "correta": "Queima do LED"},

        # 45
        {"pergunta": "A biblioteca usada para controlar servos é:",
         "alternativas": ["Servo.h", "Wire.h", "PWM.h", "Control.h", "Pins.h"],
         "correta": "Servo.h"},

        # 46
        {"pergunta": "random(0, 10) pode gerar:",
         "alternativas": ["De 0 a 9", "De 1 a 10", "Só pares", "Só ímpares", "10 a 20"],
         "correta": "De 0 a 9"},

        # 47
        {"pergunta": "A breadboard é usada para:",
         "alternativas": ["Montar circuitos sem solda", "Criar código", "Guardar sensores", "Medir tensão", "Substituir Arduino"],
         "correta": "Montar circuitos sem solda"},

        # 48
        {"pergunta": "O botão RESET serve para:",
         "alternativas": ["Reiniciar o programa", "Apagar a memória", "Criar variáveis", "Gerar PWM", "Ligar módulo Bluetooth"],
         "correta": "Reiniciar o programa"},

        # 49
        {"pergunta": "Quando um botão usa INPUT_PULLUP ele fica:",
         "alternativas": ["Em HIGH até ser pressionado", "Em LOW sempre", "Lendo valores aleatórios", "Desligado", "Impedido de funcionar"],
         "correta": "Em HIGH até ser pressionado"},

        # 50
        {"pergunta": "Para que serve um diodo?",
         "alternativas": ["Deixar corrente passar só em um sentido", "Armazenar carga", "Gerar luz", "Aumentar tensão", "Medir temperatura"],
         "correta": "Deixar corrente passar só em um sentido"},
    ]


# Função principal do quiz
def jogar_quiz(perguntas):
    print("\n INÍCIO DO QUIZ \n")
    sorteadas = random.sample(perguntas, 20)
    pontuacao = 0.0

#adiciona o numero as perguntas
    for i, p in enumerate(sorteadas, 1):
        print(f"Pergunta {i}: {p['pergunta']}")

        alternativas = p["alternativas"].copy()
        random.shuffle(alternativas)

        letras = ["A", "B", "C", "D", "E"]
        for idx, alt in enumerate(alternativas):
            print(f"{letras[idx]}) {alt}")

        resposta = input("Sua resposta (A–E): ").upper().strip()
        while resposta not in letras:
            resposta = input("Digite A, B, C, D ou E: ").upper().strip()

        if alternativas[letras.index(resposta)] == p["correta"]:
            print(" Voce acertou!\n")
            pontuacao += 0.5
        else:
            print(f" Você infelizmente errou a resposta correta é a : {p['correta']}\n")

    print("=== FIM DO QUIZ ===")
    print(f"Pontuação final: {pontuacao:.1f} / 10.0\n")


# Visualizar banco
def mostrar_banco_de_perguntas():
    banco = criar_banco()
    print("\n=== BANCO COMPLETO ===\n")
    for i, p in enumerate(banco, 1):
        print(f"{i}. {p['pergunta']}")
        for alt in p["alternativas"]:
            print(f"   - {alt}")
        print(f"   Resposta: {p['correta']}\n")


# Menu principal
def main():
    mensagem_inicial()
    banco = criar_banco()

    while True:
        print(" MENU PRINCIPAL")
        print("1 - Responder quiz")
        print("2 - Regras")
        print("3 - Encerrar")
        print("4 - Ver banco de perguntas")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            jogar_quiz(banco)
        elif opcao == "2":
            mostrar_regras()
        elif opcao == "3":
            print("\nEncerrando o programa.")
            break
        elif opcao == "4":
            mostrar_banco_de_perguntas()
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    main()

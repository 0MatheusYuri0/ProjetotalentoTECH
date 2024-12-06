# Funções para operações matemáticas
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisão por zero."

# Função principal para a calculadora
def calculadora():
    print("Selecione uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Entrada de dados
    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Verificar se a operação escolhida é válida
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")
        return

    try:
        # Solicitar os dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        return

    # Executar a operação escolhida
    if operacao == '1':
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
    elif operacao == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif operacao == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif operacao == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")

# Chama a função da calculadora
calculadora()

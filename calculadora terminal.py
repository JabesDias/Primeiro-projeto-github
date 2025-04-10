def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("=== Calculadora Simples ===")
print("Operações disponíveis:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma operação para realizar agora  (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = somar(num1, num2)
elif opcao == "2":
    resultado = subtrair(num1, num2)
elif opcao == "3":
    resultado = multiplicar(num1, num2)
elif opcao == "4":
    resultado = dividir(num1, num2)
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)
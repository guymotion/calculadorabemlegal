# Função da calculadora simples
n1 = float(input("Digite o primeiro número: "))
op = input("Escolha a operação (+, -, *, /): ")
n2 = float(input("Digite o segundo número: "))

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Erro: Divisão por zero!")

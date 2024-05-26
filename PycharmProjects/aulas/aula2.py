"""
Projeto da criação da Adega
"""
print("Projeto Calculadora")
valor1 = float(input("Digite o 1° número: "))
operacao = input("Digite a operação: ")
valor2 = float(input("Digite o 2° número: "))

if operacao == "+":
    print(f"{valor1} + {valor2} = {valor1 + valor2}")

elif operacao == "-":
    print(f"{valor1} - {valor2} = {valor1 - valor2}")

elif operacao == "*":
    print(f"{valor1} * {valor2} = {valor1 * valor2}")

elif operacao == "/":
    print(f"{valor1} / {valor2} = {valor1 / valor2}")

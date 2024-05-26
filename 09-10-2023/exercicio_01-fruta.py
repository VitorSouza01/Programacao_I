
dicionario = {1: "Banana", 2: "Maça", 3: "Pêra", 4: "Melância", 5: "Morango", 6: "Abacaxi"}

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print("Qual fruta você deseja comer?\n",
      "1° - Banana\n",
      "2° - Maça\n",
      "3° - Pêra\n",
      "4° - Melância\n",
      "5° - Morango\n",
      "6° - Abacaxi")

while True:
    fruta = int(input("Digite o número da fruta que deseja comer: "))

    if dicionario.get(fruta):
        print(f"\n{nome} tem {idade} anos e a fruta escolhida foi {dicionario[fruta]}.")
        break

    else:
        print("Esse número de fruta não existe!")

list = ["Banana", "Maça", "Pêra", "Melância", "Morango", "Abacaxi"]

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
print("Qual fruta você deseja comer?\n",
      "1° - Banana\n",
      "2° - Maça\n",
      "3° - Pêra\n",
      "4° - Melância\n",
      "5° - Morango\n",
      "6° - Abacaxi")
fruta = int(input("Digite o número da fruta que deseja comer: "))

for n in range(1):
      print(list.index(fruta))

#print(f"{nome} tem {idade} anos e escolheu {list[fruta]}.")


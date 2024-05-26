"""
Está aula possui 3 objetivos:
1.) Explicar como se comenta com o python e o por quê.
2.) Utilizar o comando print.
3.) Utilizar o comando input.
4.) Se der, variáveis.
Estes são os nossos objetivos de hoje
"""
print("O programa de hoje terá três objetivos:\n")
print("1.) Explicar como se comenta com o python e o por quê.")
print("2.) Utilizar o comando print.")
print("3.) Utilizar o comando input.")

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

#print(f"O nome do usário é {nome} e sua idade é {idade} anos.")
#print("O nome do usário é", nome, "e sua idade é", idade, "anos.")
print("O nome do usárioe é %s" % nome, "e sua idade é %i anos." % idade)
"""
if idade >= 21:'
    print("Pode comprar a pinga!!!")
elif idade >= 18:
    print("Pode comprar cerveja!!!")
else:
    print("Cai fora moloque!!!")
"""
if idade < 18:
    print("VAZA!!!")
elif idade < 21:
    print("Pode comprar cerveja!!!")
else:
    print("Pode comprar a pinga!!!")

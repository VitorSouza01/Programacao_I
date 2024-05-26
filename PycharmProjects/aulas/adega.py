"""
Nossa adega vai vender
Heineken 269ml R$ 4,52
Skol 350ml R$ 3,99
Coca-Cola 350ml R$ 3,56
"""
# Declaração das variáveis
tcompra = float(0)
loop = 0

while loop == 0:
    print("\nSeja bem vindo a Adega Hora Extra. Sua compra está no valor de: R$ %.2f" % tcompra)
    print("0 - Encerrar a Compra!")
    print("1 - Heineken 269ml: R$ 4,52")
    print("2 - Skol 350ml: R$ 3,99")
    print("3 - Coca-Cola 350ml: R$ 3,56")
    escolha = int(input("O que deseja comprar: "))

    if escolha == 1:
        qtd = int(input("Quantas Heineken deseja: "))
        tcompra += 4.52 * qtd

    elif escolha == 2:
        qtd = int(input("Quantas Skol deseja: "))
        tcompra += 3.99 * qtd

    elif escolha == 3:
        qtd = int(input("Quantas Coca-Cola deseja: "))
        tcompra += 3.56 * qtd

    elif escolha == 0:
        loop = 1

    else:
        print("Produto não existe")

else:
    print("\nTotal do Valor da Compra: R$ %.2f" % tcompra)

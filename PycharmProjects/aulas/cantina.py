"""
Cantina
Coxinha R$ 7.33
Suco de Uva R$ 9.34
"""
compra_coxinha, compra_suco = 0, 0
loop = 0

while loop == 0:
    print("\n[ Cantina Preço Barato ]")
    print("Sua compra está no valor de: R$ %.2f" % (compra_coxinha + compra_suco))
    print("0 - Encerrar a Compra!")
    print("1 - Coxinha R$ 7.33")
    print("2 - Suco de Uva R$ 9.34")
    escolha = int(input("O que deseja comprar: "))

    if escolha == 1:
        quantidade_coxinha = int(input("Quantidade de Coxinha: "))
        compra_coxinha += 7.33 * quantidade_coxinha

    elif escolha == 2:
        quantidade_suco = int(input("Quantidade de Suco de Uva: "))
        compra_suco += 9.34 * quantidade_suco

    elif escolha == 0:
        loop = 1

    else:
        print("Produto Não Existe!")

print("\n[ Resultado ]")
print(f"Quantidade de Coxinha: {quantidade_coxinha}")
print(f"Quantidade de Suco de Uva: {quantidade_suco}")
print("fValor Total Das Compras: %.2f" % (compra_coxinha + compra_suco))

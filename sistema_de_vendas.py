estoque_produto = {
    1 : {"Nome": "Monitor Mancer", "Preço": 650.00, "Quantidade": 30},
    2 : {"Nome": "Gabite Aquario", "Preço": 300.00, "Quantidade": 25},
    3 : {"Nome": "Redmagic 11 Pro", "Preço": 8999.00, "Quantidade": 35},
    4 : {"Nome": "Mouse Attack Shark", "Preço": 250.00, "Quantidade": 20},
    5 : {"Nome": "Teclado Alienware", "Preço": 200.00, "Quantidade": 20},
    6 : {"Nome": "Air Coller Aura-MAX", "Preço": 350.00, "Quantidade": 20},
    7 : {"Nome": "Fan lian-li", "Preço": 110.00, "Quantidade": 30},
    8 : {"Nome": "Rizen 5500GT", "Preço": 750.00, "Quantidade": 15},
    9 : {"Nome": "GeForce RTX 5090", "Preço": 25990.00, "Quantidade": 30},
}

carrinho = []
subtotal = 0

while True:
    print("<>"*15)
    print(" Seja Bem a minha loja")
    print("<>"*15)
    print(" [1] Visualizar estoque.")
    print(" [2] Adicionar item ao carrinho.")
    print(" [3] Visualizar carrinho.")
    print(" [4] Finalizar compra.")
    print(" [5] Sair do sistema.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("<>" * 15)
        print("Visualizando estoque!")
        print("<>" * 15)

        print(f"{"ID":<5}|{"NOME":<35}|{"VALOR":<10}|QUANTIDADE")
        for k, v in estoque_produto.items():
            print(f"{k:<5}|{v['Nome']:<35}|{v['Preço']:<10}|{v['Quantidade']} ")

    elif opcao == 2:
        print("<>" * 15)
        print("Adicionando itens ao carrinho!")
        print("<>" * 15)

        id_produto = int(input("Qual ID do produto voce deseja comprar? "))
        if id_produto in estoque_produto:
            qnt_produto = int(input("Quantas unidades você deseja? "))
            if qnt_produto <= 0:
                print("Quantidaes inválida!")
            elif qnt_produto <= estoque_produto[id_produto].get('Quantidade', 0):

                item = {
                    "qtd" : qnt_produto,
                    "nome" : estoque_produto[id_produto]["Nome"],
                    "preco" : estoque_produto[id_produto]["Preço"],
                    "preco_total" : qnt_produto * estoque_produto[id_produto]["Preço"]
                }
                carrinho.append(item)
                estoque_produto[id_produto]["Quantidade"] -= qnt_produto
                print(item)
            else:
                print(f"Quantidade indisponivel, temos apenas"
                f"{estoque_produto[id_produto]['Quantidade']} no estoque.")
        else:
            print("Id informado não existe no estoque")

    elif opcao == 3:
        if carrinho:
            print("<>" * 15)
            print("Visualizando carrinho!")
            print("<>" * 15)

            for i in carrinho:
                print(f"{i['qtd']}x {i['nome']} no valor de R$ {i['preco']:.2f} (cada)\nTotal R$ {i['preco_total']:.2f}")
                subtotal += i["preco_total"]
            print(f"Subtotal da Compra R${subtotal:.2f}")
        else:
            print("Carrinho vazio!")


    elif opcao == 4:
        if carrinho:
            print("<>" * 15)
            print("\n=== Finalizar Compra ===")
            print("<>" * 15)
            total_compra = sum(item["preco_total"] for item in carrinho)
            cupom = input("Digite um cupom (ou pressione Enter): ").upper()
            desconto = 0
            if cupom == "DEV10":
                desconto = total_compra * 0.1
                print("Cupom Valido: Voce obteve 10% de desconto.")
            elif cupom == "DEV20" and total_compra > 500:
                desconto = total_compra * 0.2
                print("Cupom valido: Voce obteve 20% de desconto.")
            elif len(cupom) == 0:
                print("Nenhum cupom adicionado.")
            else:
                print("Cupom invalido, nenhum desconto adicionado.")

            total = total_compra - desconto

            print("------RESUMO DO PEDIDO-------")
            print(f"Subtotal da compra: R${subtotal:.2f}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Valor final: R${subtotal - desconto:.2f}")
            print("-" * 30)
            carrinho.clear()
        else:
            print("Não há itens no carrinho para finalizar.")

    elif opcao == 5:
        print("<>" * 15)
        print("Encerrando!!!")
        print("<>" * 15)
        break
    else:
        print("Opção invalida")
estoque_produto = {
    1 : {"Nome": "Monitor Mancer", "Preço": 650.00, "Quantidade": 50},
    2 : {"Nome": "Gabite Aquario", "Preço": 300.00, "Quantidade": 35},
    3 : {"Nome": "Redmagic 11 Pro", "Preço": 8999.00, "Quantidade": 25},
    4 : {"Nome": "Mouse Attack Shark", "Preço": 250.00, "Quantidade": 40},
    5 : {"Nome": "Teclado Alienware", "Preço": 200.00, "Quantidade": 40},
    6 : {"Nome": "Air Coller Aura-MAX", "Preço": 350.00, "Quantidade": 20},
    7 : {"Nome": "Fan lian-li", "Preço": 110.00, "Quantidade": 50},
    8 : {"Nome": "Rizen 5500GT", "Preço": 750.00, "Quantidade": 15},
    9 : {"Nome": "GeForce RTX 5090", "Preço": 25990.00, "Quantidade": 35},
}

carrinho = []

while True:
    print("*"*30)
    print(" Seja Bem a minha loja")
    print("*"*30)
    print(" [1] Visualizar estoque.")
    print(" [2] Adicionar item ao carrinho.")
    print(" [3] Visualizar carrinho.")
    print(" [4] Finalizar compra.")
    print(" [5] Sair do sistema.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Visualizando estoque!")
        print(f"{"ID":<5}|{"NOME":<35}|{"VALOR":<10}|QUANTIDADE")
        for k, v in estoque_produto.items():
            print(f"{k:<5}|{v['Nome']:<35}|{v['Preço']:<10}|{v['Quantidade']} ")

    elif opcao == 2:
        print("Adicionando itens ao carrinho!")
        id_produto = int(input("Qual ID do produto voce deseja comprar? "))
        if id_produto in estoque_produto:
            qnt_produto = int(input("Quantas unidades você deseja? "))
            if qnt_produto <= 0:
                print("Quantidaes inválida!")
            elif qnt_produto <= estoque_produto[id_produto]['quantidade']:
                item = {
                    "qtd" : qnt_produto,
                    "nome" : estoque_produto[id_produto]["nome"],
                    "preco" : estoque_produto[id_produto]["preco"],
                    "preco_total" : qnt_produto * estoque_produto[id_produto]["preco"]
                }
                carrinho.append(item)
                estoque_produto[id_produto]["quantidade"] -= qnt_produto
                print(item)
            else:
                print(f"Quantidade indisponivel, temos apenas"
                f"{estoque_produto[id_produto]["quantidade"]} no estoque.")
        else:
            print("Id informado não existe no estoque")

    elif opcao == 3:
        if carrinho:
            print("Visualizando carrinho!")
            subtotal = 0
            for i in carrinho:
                print(f"{i['qtd']}x {i['nome']} no valor de R$ {i['preco']:.2f} (cada)\nTotal R$ {i['preco_total']:.2f}")
                subtotal += i["preco_total"]
            print(f"Subtotal da Compra R${subtotal:.2f}")
        else:
            print("Carrinho vazio!")


    elif opcao == 4:
        print("Finalizando compra!")
        if carrinho:
            subtotal = sum(i["preco_total"] for i in carrinho)
            print(f"Subtotal dos itens: R$ {subtotal:.2f}")

            tem_cupom = input("Possui cupom de desconto? (S/N): ").strip().upper()
            desconto = 0.0

            if tem_cupom == "S":
                cupom = input("Digite o cupom: ").strip().upper()
                if cupom in cupons_validos:
                    desconto = subtotal * cupons_validos[cupom]
                    print(f"Cupom {cupom} aplicado com sucesso! Desconto de R$ {desconto:.2f}")
                else:
                    print("Cupom inválido ou expirado! Prosseguindo sem desconto.")

            total_final = subtotal - desconto
            print("-" * 30)
            print(f"Total a pagar: R$ {total_final:.2f}")
            print("Compra realizada com sucesso!")
            print("-" * 30)
            carrinho.clear()
        else:
            print("Não há itens no carrinho para finalizar.")


    elif opcao == 5:
        print("Encerrando!!!")
        break
    else:
        print("Opção invalida")
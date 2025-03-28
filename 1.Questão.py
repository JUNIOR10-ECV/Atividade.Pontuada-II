
# Número da turma: 97744
# Turma; Vespertino
# Nome: Ausgusto Júnio Leite dos Santos
# Nome: Lázaro Ramos Rodrigues Ferreira



import os

os.system("cls || clear")

valor_total = 0
preco_total = 0
pratos_solicitados = ""
desconto1 = 0.1
desconto2 = 1.10

while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
    6 \t Feijoada     \t\tR$ 30,00
    7 \t Pizza        \t\tR$ 23,00
          
               """)

    opcao = int(input("Digite o número da prato desejada: "))


    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case 6:
            prato = "Feijoada"
            preco = 30
        case 7:
            prato = "Pizza"
            preco = 23
        case _:
            print("Opção inválida. \nTente novamente... \n")
            prato = ""
            preco = 0

    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == 'S':
        pratos_solicitados += 1
    if mais_pedidos == "n":
        break


print("""
=========== FORMA DE PAGAMENTO ===========
1  \tÁ Vista   
2   \tÁ Prazo        
""")

valor_do_pagamento = float(input("Digite o valorda compra: "))
print()

match valor_do_pagamento:
    case 1:    
        valor_total = preco_total * 0.1
        print(f"Valor do desconto : {desconto1}")
        print(f"Prato : {pratos_solicitados}")
        print(f"Subtotal R$: {preco_total}")
        print(f"Valor com desconto S$: {valor_total:.2f}")
    case 2:
        valor_total1 = preco_total * desconto2
        print(f"Valor do desconto : {desconto2}")
        print(f"Prato : {pratos_solicitados}")
        print(f"Subtotal R$: {preco_total}")
        print(f"Valaor com acréscimo R$: {valor_total1:.2f}")




# Exibir resultados




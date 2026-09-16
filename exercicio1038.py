# Escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

CODIGO, QUANTIDADE = map(int, input().split())

if CODIGO == 1:
    PRECO = 4.00
elif CODIGO == 2:
    PRECO = 4.50
elif CODIGO == 3:
    PRECO = 5.00
elif CODIGO == 4:
    PRECO = 2.00
elif CODIGO == 5:
    PRECO = 1.50
    
TOTAL = QUANTIDADE * PRECO

print(f"Total: R$ {TOTAL:.2f}")
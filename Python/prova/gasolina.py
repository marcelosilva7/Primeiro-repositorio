litros = float(input('Quantos litros vai abastecer ? '))
tipo = input('De que tipo [G/A]? ').lower()
gasolina = 3.3
alcol = 2.9
if tipo == 'a':
    if litros > 20:
        desconto1 = alcol * 0.05
        preco1 = alcol - desconto1
        print(f'o preço com desconto é {preco1} total {preco1 * litros}')
    else:
        desconto = alcol * 0.03
        preco = alcol - desconto
        print(f'o preço com desconto é {preco}totalizndo{preco * litros}')
elif tipo == 'g':
    if litros > 20:
        desconto3 = gasolina * 0.06
        preco3 = gasolina - desconto3
        print(f'o preço com desconto é {preco3} total {preco3 * litros}')
    else:
        desconto2 = gasolina * 0.04
        preco2 = gasolina - desconto2
        print(f'o preço com desconto é {preco2} total {preco2 * litros}')
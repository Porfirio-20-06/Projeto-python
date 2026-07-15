# Variavel

valor_compra = int(input("Digite o valor da compra: "))

if valor_compra > 1000:
    print('frete gratis')

elif valor_compra > 800:
    print('frete com 80% de desconto')

elif valor_compra > 400:
    print('frete com 50% de desconto')

elif valor_compra > 200:
    print('frete com 15% de desconto')

else:
    print('frete sem desconto')
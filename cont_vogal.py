frase = input('Digite um frase: ')

vogais = 'aeiouAEIOU'
contagem = 0
for car in frase:
    if car in vogais:
        contagem += 1
print(f'A frase "{frase}" tem {contagem} vogais.')
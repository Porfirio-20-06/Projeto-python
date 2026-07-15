# Frequência de caracteres em uma frase 

frase = input('Digite uma frase: ')

frequencia = {}
for letra in frase:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(f'A frequência de cada caractere em "{frase}" é:')
for caractere, contagem in frequencia.items():
    print(f'"{caractere}": {contagem}')
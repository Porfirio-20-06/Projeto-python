palavra = input("Digite uma palavra: ")

palindromo = palavra == palavra[::-1]
print(f'A palavra "{palavra}" é um palíndromo? {palindromo}')
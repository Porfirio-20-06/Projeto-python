nota = [int(input(f'Digite a nota {i+1}: ')) for i in range(10)]

media = sum(nota) / len(nota)
print(f'A média das notas é: {media:.2f}')
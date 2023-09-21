def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

num_notas = int(input("Digite o número de notas: "))

notas = []

for i in range(num_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media_notas = calcular_media(notas)
print(f"A média das notas é {media_notas:.2f}")
alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    alunos[nome] = nota

soma_notas = 0

for nota in alunos.values():
    soma_notas += nota

media = soma_notas / len(alunos)

print("Dicionário de Alunos:", alunos)
print("Soma das Notas:", soma_notas)
print("Média das Notas:", media)


nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: ")) 
altura = float(input("Digite sua altura: "))  
peso = float(input("Digite seu peso: "))  

maior_de_idade = idade >= 18

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Peso:", peso, "quilogramas")
print("Maior de idade:", "Sim" if maior_de_idade else "Não")
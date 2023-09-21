
peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Seu peso está saudável")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso")
elif 30 <= imc < 34.9:
    print("Você está com obesidade tipo 1")
elif 35 <= imc < 39.9:
    print("Você está com obesidade tipo 2")
else:
    print("Você está com obesidade tipo 3")
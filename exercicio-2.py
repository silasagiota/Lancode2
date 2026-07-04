#lan code video 2
# usar o if, lendo codigo linha 5 se a idade for maior que 17 rode o texte maior de idade
#else significa se nao

idade = int(input("digite sua idade "))
if idade>17:
    print("maior de idade")
else:
    print("Voce e de menor")

# operadores de comparacao
# o simbolo de dois =  e um operador de comparação
nome = input("Digite seu nome ")

if nome == "Silas":
    print("Nome Perfeito!!!")

#no caso de notas como exemplo tem que ser usado o float pois sao numero decimais

nota = float(input("Digite sua nota!"))
if nota >=6:
    print("Passou!")
else:
    print("Não passou!")
# diferencas entre if, else, elif

idade = int(input("digite sua idade"))

if idade < 13:
    print("Criança")
elif idade < 18:
    print("adolescente")
elif idade < 65:
    print("adulto")
else:
    print("idoso")

#booleano
#condiçoes verdadeiras e falsas

resultado = 19 < 5
print(resultado)

resultado = 3 < 5
print(resultado)




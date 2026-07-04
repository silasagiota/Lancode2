#operadores logicos
# and usado como e junção
idade = 19
tem_carteira_motorista = True

if idade >=18 and tem_carteira_motorista:
    print(" Você está habilitado, ou seja, pode dirigir! ")

    # or usado como ou exemplo a seguir para cinema meia entrada

estudante = True
idoso = False

if estudante or idoso:
    print("Você paga meia")
else:
    print("Vai pagar integral")

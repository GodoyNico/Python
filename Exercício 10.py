#10- Elabore um algorítmo que dada a idade de um nadado classifique-o em uma das seguintes categorias:

#Infantil-a = 5 a 7 anos
#Infantil-b = 8 a 11 anos
#Juvenil-a = 12 a 13 anos
#Juvenil-b = 14 a 17 anos
#Adultos = Maiores de 18 anos

idade=int(input('Insira a idade do atleta: '))
print()

if 0<idade<17:
    if 0<idade<5:
        print('Atleta sem idade suficiente para competir!')
    if 5<=idade<=7:
        print('Alteta inscrito na categoria: Infantil-A')
    if 8<=idade<=11:
        print('Alteta inscrito na categoria: Infantil-B')
    if 12<=idade<=13:
        print('Alteta inscrito na categoria: Juvenil-A')
    if 14<=idade<=17:
        print('Alteta inscrito na categoria: Juvenil-B')
else:
    print('Alteta inscrito na categoria: Adulto')


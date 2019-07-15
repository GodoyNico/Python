#9- A Secretaria do Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente 
#poluentes do meio ambiente. O índice de poluição aceitável varia de 0.05 até 0.25. Se o índice sobe para 0.3 as
#indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0.4 as indústrias do 1º e 2º
#grupo são intimadas a suspenderem suas atividades, se o indice atingir 0.5 todos os grupos devem ser notificados a
#paralisarem suas atividades. Faça um algorítmo que leia o índice de poluição medido e emita a notificação adequada aos
#diferentes grupos de empresas.

indice=float(input('Insira o valor do índice de poluição: '))

if 0.3<=indice<0.4:
    print('Grupo 1, encerrar atividades!')

if 0.4<=indice<0.5:
    print('Grupos 1 e 2, encerrar atividades!')

if 0.5<=indice:
    print('Todos os grupos, encerrar atividades!')

if 0.05<=indice<=0.25:
    print('Indice normal, prossigam!')

if 0.26<=indice<0.3:
    print('Indices elevados, cuidado!')

#Inserir while para pedir várias variaveis

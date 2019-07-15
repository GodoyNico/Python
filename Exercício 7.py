#7- Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas
#sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado
#de cada um deles, para verificar o que se pode aproveitar deles. Foi requisitado que você desenvolva um programa para registrar este
#levantamento. O programa deverá receber um número indeterminado de entradas, cada um contendo: um número de identificação do mouse e o
#tipo de defeito:

    #- Necessita da esfera;
    #- Necessita de limpeza;
    #- Necessita troca do cabo ou conector;
    #- Quebrado ou inutilizado.

#Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

    #Quantidade de mouses: 100

    #Situação                                        Quantidade      Percentual
    #1- Necessita de esfera                              40              40%
    #2- Necessita de limpeza                             30              30%
    #3- Necessita troda do cabo ou conector              15              15%
    #4- Quebrado ou inutilizado                          15              15%

identif_mouse=int(input('Insira o ID do mouse: '))
quantidade=0
necessita_esfera=0
necessita_limpeza=0
necessita_troca_cabo=0
quebrado=0

while identif_mouse != 0:
    print('Identifique o defeito: ')
    print('1- Necessita esfera')
    print('2- Necessita limpeza')
    print('3- Necessita troca do cabo ou conector')
    print('4- Quebrado ou inutilizado')
    defeito=int(input('Insira o defeito: '))

    if defeito == 1:
        necessita_esfera=necessita_esfera+1
    if defeito == 2:
        necessita_limpeza=necessita_limpeza+1
    if defeito == 3:
        necessita_troca_cabo=necessita_troca_cabo+1
    if defeito == 4:
        quebrado=quebrado+1
    quantidade=quantidade+1
    identif_mouse=int(input('Insira o ID do mouse: '))

percentual_esfera=(necessita_esfera*100)/quantidade
percentual_limpeza=(necessita_limpeza*100)/quantidade
percentual_cabo=(necessita_troca_cabo*100)/quantidade
percentual_defeito=(defeito*100)/quantidade

print('Quantidade de mouses: {0}'.format(quantidade))
print('Situação                                     Quantidade          Percentual')
print('1- Necessita esfera:                             {0}                 {1:.2f}%'.format(necessita_esfera,percentual_esfera))
print('2- Necessita limpeza:                            {0}                 {1:.2f}%'.format(necessita_limpeza,percentual_limpeza))
print('3- Necessita troca de cabo ou conector:          {0}                 {1:.2f}%'.format(necessita_troca_cabo,percentual_cabo))
print('4- Quebrado:                                     {0}                 {1:.2f}%'.format(quebrado,percentual_defeito))


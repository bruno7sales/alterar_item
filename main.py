# Lista
nomes = ['Fulano', 'Ciclano', 'Beltrano', 'João', 'Maria', 'Jose']
while True:
# Exibir a lista e seus respectivos indices:
    for i in range(len(nomes)):
        print(f'Indicie {i}: {nomes[i]}.')

# Quebra d elinha
    print('\n')

    try:
        #usuario informa indice
        indice = int(input('Informe o numero do indice: '))

        # Faz a alteração
        nomes[indice] = input('informe o novo nome: ').capitalize()
    except:
        print('Não possivel fazer a alteração!')
    print('\n')
    # Exibe a nova lista
    for i in range(len(nomes)):
        print(f'Indicei {i}: {nomes[i]}.')
    
    #verifica se p usúario deseja continuar
    continuar = input('Deseja continuar (s/n)').lower()

    # Verifica a opção do usúario
    if continuar == 's':
        continue
    else:
        break

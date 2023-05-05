def intro_duvida(opcoes):
    while True:
        print(*opcoes, sep='\n')
        duvida = input('\nDigite um número: ')
        if duvida not in ['1', '2', '3', '4']:
            print('ERRO! Número inválido, tente novamente entre 1 a 4')
        else:
            return duvida

def intro_consulta(opcoes):
    while True:
        print(*opcoes, sep='\n')
        consulta = input('\nDigite um número: ')
        if consulta not in ['1', '2', '3', '4', '5']:
            print('ERRO! Número inválido, tente novamente entre 1 a 5')
        else:
            return consulta

def saida_volta():
    while True:
        print('\n 1_ Voltar\n 2_ Voltar ao início \n 3_ Sair')
        saida = input('\nDigite um número: ')
        if saida == '1':
            break
        elif saida == '2':
            return True
        elif saida == '3':
            return '4'

#// PRINCIPAL
voltar_inicio = False
consulta = ''
duvida = ''

while True:
    if duvida == '4' or consulta == '5':
        break

    opcoes = ['1_ Dúvidas sobre Codewars',
              '2_ Dúvidas sobre Discord',
              '3_ Dúvidas sobre as aulas',
              '4_ Sair']

    duvida = intro_duvida(opcoes)
    if duvida == '4' or consulta == '5':
        break

    if duvida == '1':
        opcoes = ['1_ link de acesso?',
                  '2_ Classificação?',
                  '3_ Quais tecnologias treinar?',
                  '4_ Retornar ao início',
                  '5_ Sair']

        while True:
            consulta = intro_consulta(opcoes)
            if consulta in ['4', '5']:
                break
            if consulta == '1':
                print('Resposta para "link de acesso?"')
            elif consulta == '2':
                print('Resposta para "Classificação?"')
            elif consulta == '3':
                print('Resposta para "Quais tecnologias treinar?"')

            voltar_inicio = saida_volta()
            if voltar_inicio:
                break
                    
print('Obrigado, volte sempre!!!')

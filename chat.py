while True:                                                         #Enquanto verdade, repete para sempre
    print('[ 1 ] 0\n'
          '[ 2 ] 0\n'
          '[ 3 ] 0\n'
          '[ 4 ] Sair')

    resposta = input('Digite um número: ')[0]                       #Atribui um valor a 'resposta'
    if resposta == '4':                                             #Enterrompe o loop se 'resposta' for igual a 4
        break
    if resposta not in '1234':                                      #se 'resposta' não estiver dentro de '1234' então imprima 
        print('ERRO! Número invalido, tente novamente!')

    if resposta == '1':                                             #se 'resposta' for igual a '1' então
        while True:                                                 #loop repita sempre
            print('[ 1 ] 1\n'
                  '[ 2 ] 1\n'
                  '[ 3 ] 1\n'
                  '[ 4 ] Sair')

            resposta = input('Digite um número: ')[0]               #Atribui um valor a 'resposta'
            if resposta == '4':                                     #Enterrompe o loop se 'resposta' for igual a 4
                resposta = ''                                       #Limpra a vareavel pra não interferir quando volta pro loop, linha: 2
                break
            if resposta not in '1234':                              #se 'resposta' não estiver dentro de '1234' então imprima 
                print('ERRO! Número invalido, tente novamente!')

            if resposta == '1':                                     #se 'resposta' for igual a '1' então
                while True:                                         #lopp repita sempre
                    print('[ 1 ] 1.1\n'
                          '[ 2 ] 1.1\n'
                          '[ 3 ] 1.1\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]       #Atribui um valor a 'resposta'
                    if resposta == '4':                             #Enterrompe o loop se 'resposta' for igual a 4
                        resposta = ''                               #Limpra a vareavel pra não interferir quando volta pro loop, linha: 14
                        break                              
                    if resposta not in '1234':                      #se 'resposta' não estiver dentro de '1234' então imprima
                        print('ERRO! Número invalido, tente novamente')  

                    if int(resposta) == 1:                          #se o int(resposta) for igual a '1' então imprima
                        print('1.1.1')
                    elif int(resposta) == 2:                        #se o int(resposta) for igual a '2' então imprima
                        print('1.1.2')
                    elif int(resposta) == 3:                        #se o int(resposta) for igual a '3' então imprima
                        print('1.1.3')

            elif resposta == '2':                                     #se 'resposta' for igual a '1' então
                while True:                                           #loop repita sempre
                    print('[ 1 ] 1.2\n'
                          '[ 2 ] 1.2\n'
                          '[ 3 ] 1.2\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]       #Atribui um valor a 'resposta'
                    if resposta == '4':                             #Enterrompe o loop se 'resposta' for igual a 4
                        resposta = ''                               #Limpra a vareavel pra não interferir quando volta pro loop, linha: 14
                        break
                    if resposta not in '1234':                      #se 'resposta' não estiver dentro de '1234' então imprima ERRO                     
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:                          #se o int(resposta) for igual a '1' então imprima
                        print('1.2.1')
                    elif int(resposta) == 2:                        #se o int(resposta) for igual a '2' então imprima
                        print('1.2.2')
                    elif int(resposta) == 3:                        #se o int(resposta) for igual a '3' então imprima
                        print('1.2.3')

            elif resposta == '3':                                   #se 'resposta' for igual a '1' então
                while True:                                         #loop repita sempre
                    print('[ 1 ] 1.3\n'
                          '[ 2 ] 1.3\n'
                          '[ 3 ] 1.3\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]       #Atribui um valor a 'resposta'
                    if resposta == '4':                             #Enterrompe o loop se 'resposta' for igual a 4
                        resposta = ''                               #Limpra a vareavel pra não interferir quando volta pro loop, linha: 14
                        break
                    if resposta not in '1234':                      #se 'resposta' não estiver dentro de '1234' então imprima ERRO
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:                          #se o int(resposta) for igual a '1' então imprima
                        print('1.3.1')
                    elif int(resposta) == 2:                        #se o int(resposta) for igual a '2' então imprima
                        print('1.3.2')
                    elif int(resposta) == 3:                        #se o int(resposta) for igual a '3' então imprima                      
                        print('1.3.3')
    
    elif resposta == '2':
        while True:
            print('[ 1 ] 2\n'
                  '[ 2 ] 2\n'
                  '[ 3 ] 2\n'
                  '[ 4 ] Sair')

            resposta = input('Digite um número: ')[0]
            if resposta == '4':
                resposta = ''
                break
            if resposta not in '1234':
                print('ERRO! Número invalido, tente novamente!')

            if resposta == '1':
                while True:
                    print('[ 1 ] 2.1\n'
                          '[ 2 ] 2.1\n'
                          '[ 3] 2.1\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]
                    if resposta == '4':
                        resposta = ''
                        break
                    if resposta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:
                        print('2.1.1')
                    elif int(resposta) == 2:
                        print('2.1.2')
                    elif int(resposta) == 3:
                        print('2.1.3')

            if resposta == '2':
                while True:
                    print('[ 1 ] 2.2\n'
                          '[ 2 ] 2.2\n'
                          '[ 3 ] 2.2\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]
                    if resposta == '4':
                        resposta = ''
                        break
                    if resposta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:
                        print('2.2.1')
                    elif int(resposta) == 2:
                        print('2.2.2')
                    elif int(resposta) == 3:
                        print('2.2.3')

            if resposta == '3':
                while True:
                    print('[ 1 ] 2.3\n'
                          '[ 2 ] 2.3\n'
                          '[ 3 ] 2.3\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]
                    if resposta == '4':
                        resposta = ''
                        break
                    if resposta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:
                        print('2.3.1')
                    elif int(resposta) == 2:
                        print('2.3.2')
                    elif int(resposta) == 3:
                        print('2.3.3')
                    
    elif resposta == '3':
        while True:
            print('[ 1 ] 3\n'
                  '[ 2 ] 3\n'
                  '[ 3 ] 3\n'
                  '[ 4 ] Sair')

            resposta = input('Digite um número: ')[0]
            if resposta == '4':
                resposta = ''
                break
            if resposta not in '1234':
                print('ERRO! Número invalido, tente novamente!')

            if resposta == '1':
                while True:
                    print('[ 1 ] 3.1\n'
                          '[ 2 ] 3.1\n'
                          '[ 3 ] 3.1\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]
                    if resposta == '4':
                        resposta = ''
                        break
                    if resposta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:
                        print('3.1.1')
                    elif int(resposta) == 2:
                        print('3.1.2')
                    elif int(resposta) == 3:
                        print('3.1.3')

            if resposta == '2':
                while True:
                    print('[ 1 ] 3.2\n'
                          '[ 2 ] 3.2\n'
                          '[ 3 ] 3.2\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]
                    if resposta == '4':
                        resposta = ''
                        break
                    if resposta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:
                        print('3.2.1')
                    elif int(resposta) == 2:
                        print('3.2.2')
                    elif int(resposta) == 3:
                        print('3.2.3')

            if resposta == '3':
                while True:
                    print('[ 1 ] 3.3\n'
                          '[ 2 ] 3.3\n'
                          '[ 3 ] 3.3\n'
                          '[ 4 ] Sair')

                    resposta = input('Digite um número: ')[0]
                    if resposta == '4':
                        resposta = ''
                        break
                    if resposta not in '1234':
                        print('ERRO! Número invalido, tente novamente!')

                    if int(resposta) == 1:
                        print('3.3.1')
                    elif int(resposta) == 2:
                        print('3.3.2')
                    elif int(resposta) == 3:
                        print('3.3.3')
                    
print('Obrigado, volte sempre!!!')
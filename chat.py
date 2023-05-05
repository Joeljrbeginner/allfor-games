while True:                                         
    print('[ 1 ] Dúvidas sobre codewars\n'
          '[ 2 ] Dúvidas sobre discord\n'
          '[ 3 ] Dúvidas sobre as aulas\n'
          '[ 4 ] Sair')

    assunto = input('Digite um número: ')[0]        
    if assunto == '4':              
        break
    if assunto not in '1234':        
        print('ERRO! Número invalido, tente novamente!')

    if assunto == '1':              
        while True:                 
            print('[ 1 ] link de acesso?\n'
                  '[ 2 ] Pontuação esperada?\n'
                  '[ 3 ] Quais tecnologias treinar?\n'
                  '[ 4 ] Retornar ao início')

            pergunta = input('Digite um número: ')[0]       
            if pergunta == '4':                             
                break
            if pergunta not in '1234':                      
                print('ERRO! Número invalido, tente novamente!')

            if int(pergunta) == 1:                          
                print('Link de acesso do Qualified é: https://codewars.coom')
            elif int(pergunta) == 2:                        
                print('Assunto 1, pergunta 2')
            elif int(pergunta) == 3:                       
                print('Assunto 1, pergunta 2') 
    
    elif assunto == '2':
        while True:
            print('[ 1 ] Assunto 2, pergunta 1\n'
                  '[ 2 ] Assunto 2, pergunta 2\n'
                  '[ 3 ] Assunto 2, pergunta 3\n'
                  '[ 4 ] Retornar ao início')
            
            pergunta = input('Digite um número: ')[0]
            if pergunta == '4':
                pergunta = ''
                break
            if pergunta not in '1234':
                print('ERRO! Número invalido, tente novamente!')

            if int(pergunta) == 1:
                print('Resposta: Assunto 2, pergunta 1')
            elif int(pergunta) == 2:
                print('Resposta: Assunto 2, pergunta 2')
            elif int(pergunta) == 3:
                print('Resposta: Assunto 2, pergunta 3')
                    
    elif assunto == '3':
        while True:
            print('[ 1 ] Assunto 3, pergunta 1\n'
                  '[ 2 ] Assunto 3, pergunta 1\n'
                  '[ 3 ] Assunto 3, pergunta 1\n'
                  '[ 4 ] Retornar ao início')

            pergunta = input('Digite um número: ')[0]
            if pergunta == '4':
                pergunta = ''
                break
            if pergunta not in '1234':
                print('ERRO! Número invalido, tente novamente!')


            if int(pergunta) == 1:
                print('Resposta: Assunto 3, pergunta 1')
            elif int(pergunta) == 2:
                print('Resposta: Assunto 3, pergunta 2')
            elif int(pergunta) == 3:
                print('Resposta: Assunto 3, pergunta 3')
                    
print('Obrigado, volte sempre!!!')
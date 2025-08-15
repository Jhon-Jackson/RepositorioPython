nome = str(input('Qual seu nome? '))
if nome == 'Jhon':
    print('Que nome LLlindo, seu gostoso!')
elif nome == 'Samuel' or nome == 'Johnson' or nome == 'Sivana':
    print(' Seu nome é bem popular no brasil')
elif nome in 'Larice cristine mendes':
    print(f'Voce é muito gostosa \033[35m{nome}')
else:
    print('Seu nome é bem normal.')
print('\033[4;35mTenha uma otima tarde!!')
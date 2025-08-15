from EX115.lib.interface import *
from EX115.lib.arquivo import *
from time import sleep

from utilidadesCeV.dado import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteudo de um arquivo
        lerArqivo(arq)
        cabeçalho('Opção 1')
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO! digite uma opção válida\033[31m')
    sleep(2)
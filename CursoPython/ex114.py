# Exercício Python 114:
# Crie um código em Python que teste se o site pudim está acessível
# pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://minhaconta.levelupgames.com.br/web')
# except urllib.error.ERLError:
except:
    print('O site não está acessivel no momento')
else:
    print('Consegui acessar o site com sucesso!')
    #print(site.read())
# help(urllib)
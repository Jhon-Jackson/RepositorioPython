# Nessa aula,
# vamos ver como o Python permite tratar erros e criar respostas a
# essas exceções. Aprenda como usar a estrutura try except no Python
# de uma forma simples.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except:
#   print(f'Infelizmente tivemos um problema')
except Exception as erro:
     print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferio não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')

else: # opcional
    print(f'o resultado é {r:.1f}')
finally: # opcional
    print('Volte sempre! muito obrigado')


km = int(input('Digite quantos KM vc pecorreu: '))
Mt = 80
if km > Mt:
    Div = (km - Mt) * 7
    print(f'Mutado!! voce utrapassou imite de {Mt}KM e esta devendo {Div} Reias')
else:
    print('Bomdia , dirija com cuidado!')

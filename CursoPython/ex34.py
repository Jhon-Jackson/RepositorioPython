Sa = float(input('Digite sua mesada para aumento: '))
if Sa <= 1250:
    SM = Sa +  (Sa * 15/100)
else:
    SM = Sa + (Sa * 10/100)
print(f'quem ganhava {Sa:.2f} passa a ganhar {SM:.2f}')

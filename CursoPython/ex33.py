n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
M = n1
MM = n3
# menor valor verificando
if n2<n1 and n2<n3:
    M = n2
if n3<n1 and n3<n2:
    M = n3
# maior valor verificando
if n1>n2 and n1>n3:
    MM = n1
if n2>n1 and n2>n3:
    MM = n2

print(f'menor valor {M}')
print(f'maior vallor {MM}')

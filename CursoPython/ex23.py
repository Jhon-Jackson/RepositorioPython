#Exercício Python 23:
# Faça um programa que leia um número de
# 0 a 9999 e mostre na tela cada um dos
# dígitos separados.
num = int(input('informe um numero: '))
n = str(num)
print(f'analizando o numero: {num}')
print(f'unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'centena: {n[1]}')
print(f'Milhar: {n[0]}')

num = int(input('informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'analizando o numero: {num}')
print(f'unidade: {u}')
print(f'Dezena: {d}')
print(f'centena: {c}')
print(f'Milhar: {m}')

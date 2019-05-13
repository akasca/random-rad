#carro
from math import ceil
carrop = float(input('Quanto custa o carro? \n'))
carropa = int(input('Em Quantos Meses Você Quer Parcelar o Carro? \n'))
carropar = carrop / carropa
print('Vai parcelar em {} meses, Cada Parcela Vai Ser R${}.'.format(carropa, ceil(carropar)))
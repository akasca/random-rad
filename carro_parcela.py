#carro
from math import ceil
carrop = float(input('Quanto custa o carro? \n'))
carropa = int(input('Em Quantos Meses Você Quer Parcelar o Carro? \n'))
carropar = carrop / carropa
print(f'Você Parcelou em {carropa} vezes, A parcela é {carropar}, O Carro Custa {carrop}!')

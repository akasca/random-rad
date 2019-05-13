age = int(input('Em Que Ano Você Nasceu? \n (Ex: 99 para 1999.) \n'))
#age1 = 2019 - age
#print(f'Você tem {age1} anos')
print(f'Você tem {2019 - age} anos!')

if age == 2001:
    print('Você já deve se apresentar no exército!')
elif age > 2001:
    print(f'Já passou {age - 18} de você se alistar no exército.')
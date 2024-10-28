# name = input ('digite seu nome')

# if name == "pedro":

#     print('ola,pedro')

# login = input("digite o login")

# senha = input('digite sua senha')

# if login == 'admin' and senha == '1234':

#     print('login realizado com sucesso')
# else:
#     print('login ou senha incorreto')

# idade =int(input('digite sua idade'))
# if idade <=11:
#         print('criança')
# elif idade <=17:
#         print('adolescente')
# elif idade <=59:
#         print('adulto')
# else:
#     print('idoso')

# periodo = input('digite o seu periodo de aula:')
# if periodo == ('m'):
#     print('bom dia!')
# elif periodo == ('v'):
#     print('boa tarde!')
# elif periodo == ('n'):
#     print('boa noite!')
# else:
#     print('peridodo invalido!')

tempo = int(input('digite o mes do ano!'))

if tempo  >=3 and tempo <=5 :
    print('outono')
elif tempo >=6 and tempo <=8 :
    print('inverno')
elif tempo >=9 and tempo <=11 :
    print('primavera')
elif tempo ==12 or tempo ==1 or tempo ==2 :
    print('verão')
else:
    print('mes invalido')
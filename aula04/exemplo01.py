# # Estrutura If
# idade = int(input('Insira a idade: '))

# if idade >=18:
#     print( 'Você é adulto')
# else:
#     print('Você não é adulto')

#-------------------------------------------
    
# pontos = int(input('Insira a pontuação'))
# if pontos >= 100:
#     print('Excelente!')
# elif pontos >= 50:
#     print('Bom desempenho')
# elif pontos >= 25:
#     print('Satisfatório')
# else:
#     print('Pratique mais.')

#----------------------------------------------------
#Operadores AND e OR

# usuario = input('Nome: ')
# senha = input ('Senha: ')

# if usuario == "admin" and senha == "1234":
#     print('Login realizado com sucesso')
# else:
#     print("Usuário ou senha incorretos")
#----------------------------------------------------

usuario = input('Nome: ').lower()
senha = input ('Senha: ')

if usuario == "admin" or senha == "1234":
    print('Login realizado com sucesso')
else:
    print("Usuário ou senha incorretos")
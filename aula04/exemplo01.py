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

# usuario = input('Nome: ').lower()
# senha = input ('Senha: ')

# if usuario == "admin" or senha == "1234":
#     print('Login realizado com sucesso')
# else:
#     print("Usuário ou senha incorretos")
#--------------------------------------------

# Exemplo IFs encadeados

# nota = float(input ("Insira nota: "))
# if nota >= 9:
#     print("A")
# elif nota >= 7:
#     print ("B")
# elif nota >= 5:
#     print ("C")
# elif nota >= 3:
#     print ("D")
# else:
#     print ("E")

#--------------------------------------------
# Exemplo IFs não encadeados
# nota = float(input ("Insira nota: "))
# if nota >= 9:
#     print("A")
# if nota >= 7:
#     print ("B")
# if nota >= 5:
#     print ("C")
# if nota >= 3:
#     print ("D")
# else:
#     print ("E")

#--------------------------------------------
#Exemplo IFs aninhados

nota = float(input ("Insira nota: "))
frequencia = float(input ("Informe a frequência: "))

if nota >= 7: #aprovado por nota mas precisa checar a frequência
    if frequencia >= 75:
        print('Aprovado por nota e frequência')
    else:
        print('Reprovado por frequência baixa')
else:
    print("Reprovado por nota baixa")

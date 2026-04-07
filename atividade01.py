valor = float(input('Insira o valor'))

if valor > 250:
    desconto = valor*0.16
else:
    desconto = 0

valor_final = valor - desconto
print(desconto)
print(f"O Valor final é de R${valor_final} ")
      

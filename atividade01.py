valor = float( input('Insira o valor: '))

if valor > 250:
    desconto = valor*0.16
    valor_final = valor - desconto
    print(f"O Valor final é de R$ {valor:.2f}, e com R${desconto:.2f} de desconto fica no valor de R${valor_final:.2f}")
else:
    desconto = 0
    valor_final = valor - desconto
    print("Não há desconto")
    print(f"O Valor final é de R${valor_final:.2f}")
      


valor = float( input('Insira o valor: '))
forma_de_pagamento = str( input ("Insira a forma de pagamento: a vista ou a prazo: ").lower().strip())

if valor > 250 and forma_de_pagamento == "avista":
    desconto = valor*0.16
    valor_final = valor - desconto
    print(f"O Valor é de R$ {valor:.2f}, e com R${desconto:.2f} de desconto fica no valor final de R${valor_final:.2f}")
else:
    desconto = 0
    valor_final = valor - desconto
    print("Não há desconto")
    print(f"O Valor final é de R${valor_final:.2f}")
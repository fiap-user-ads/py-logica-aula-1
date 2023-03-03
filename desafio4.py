"""
    DADOS UM VALOR E O PERCENTUAL, CALCULAR A PORCENTAGEM

    Ex:
    num = 100
    porcentagem = 20
    resultado = 20
"""

# obter valor e porcentagem
num = float(input("insira um valor: "))
porcentagem = float(input("insira a porcentagem: "))

# calcular
resultado = num / 100 * porcentagem

# exibir os resultados
print("o valor é: ", resultado)
# Coletamos a quantidade de litros e o tipo de combustível,
# já deixando o caractere em maiúsculo para facilitar nossa análise
quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
tipo_combustivel = input('Informe o tipo de combustível (E para etanol, D para diesel, GC para gasolina comum, GA para gasolina aditivada): ').upper()

# Verificamos primeiro o tipo de combustível
if tipo_combustivel == 'E':
    # Taxamos o valor do preço em litros do etanol
    preco_litro = 3.85
    # De acordo com o valor da quantidade de litros, taxamos também o desconto
    if quantidade_litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04
elif tipo_combustivel == 'D':
    # Taxamos o valor do preço em litros do diesel
    preco_litro = 5.90
    # De acordo com o valor da quantidade de litros, taxamos também o desconto
    if quantidade_litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo_combustivel == 'GC':
    # Taxamos o valor do preço em litros da gasolina comum
    preco_litro = 5.55
    # De acordo com o valor da quantidade de litros, taxamos também o desconto
    if quantidade_litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo_combustivel == 'GA':
    # Taxamos o valor do preço em litros da gasolina aditivada
    preco_litro = 5.70
    # De acordo com o valor da quantidade de litros, taxamos também o desconto
    if quantidade_litros <= 15:
        desconto = 0.04
    else:
        desconto = 0.06
# Caso ocorra um erro na especificação de tipo de combustível,
# consideramos entradas inválidas, e os preços são taxados em 0
else:
    print('Entradas inválidas!')
    preco_litro = 0
    desconto = 0

# Fazemos o cálculo do valor de desconto, seguido do cálculo do preço descontado
valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto

# Resultado
print(f'Valor a ser pago pelo cliente: R$ {valor_pago:.2f}')


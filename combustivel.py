def calcular_vantagem_gasolina_alcool(preco_gasolina, preco_alcool):
    # Calcula a relação entre o preço do álcool e o preço da gasolina, em porcentagem
    vantagem = (preco_alcool / preco_gasolina) * 100
    
    # Verifica se o preço do álcool é maior que 70% do preço da gasolina
    if preco_alcool > 0.7 * preco_gasolina:
        return "Gasolina", vantagem
    else:
        return "Álcool", vantagem

# Solicita ao usuário o valor da gasolina e do álcool
gasolina = float(input("Valor da gasolina: "))
alcool = float(input("Valor do álcool: "))

# Chama a função para calcular a vantagem entre gasolina e álcool
combustivel, vantagem = calcular_vantagem_gasolina_alcool(gasolina, alcool)

# Imprime o resultado
print(f"{combustivel} é mais vantajoso, pois a conversão resulta em {vantagem:.2f}%")

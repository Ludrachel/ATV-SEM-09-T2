def desconto(valor_x, price):
    if valor_x > 8 or price > 25:
        return price - ((price * 10) / 100)
    return price

def price_fruit(valor_x, valor_y):
    price_morango = 2.50 if valor_x <= 5 else 2.20
    price_maca = 1.80 if valor_y <= 5 else 1.50
    return desconto(valor_x + valor_y, (valor_x * price_morango) + (valor_y * price_maca))


morango = float(input())
maca = float(input())
valor = price_fruit(morango, maca)
print(f'{valor:.2f}')

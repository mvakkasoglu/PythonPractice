
price = int(input("enter price: "))


def calc_price(price) -> int:
    tax = 8.875
    price_after_tax = price + (price * tax / 100)
    return price_after_tax


print(round(calc_price(price), 2))
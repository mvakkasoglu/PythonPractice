
def money_explained():
    money = int(float(input("enter amount: "))*100)
    dollars = money// 100
    money = money % 100
    quarters = money // 25
    money = money % 25
    dimes = money // 10
    money = money % 10
    nickels = money // 5
    cents = money % 5

    print("{} dollars, {} quarters, {} dimes, {} nickels, {} cents".format(dollars, quarters, dimes, nickels, cents))


money_explained()

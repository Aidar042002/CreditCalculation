print("Программа для расчета аннуитетного и дифференцированного платежей \nПри наличии первого взноса при вводе"
      "суммы кредита нужно указать полную сумму с первым взносом")


print("Введите вид платежа '1'(аннуитетный) или '2'(дифференцированный)")
change = input()


creditAmount =0
yearAmount = 0
percent = 0
initialAmount = 0

def annuitet():
    print("Введите сумму кредита:")
    creditAmount = input()
    print("Введите количество месяцев:")
    yearAmount = input()
    print("Введите процентную ставку:")
    percent = input()
    print("Введите первоначальный взнос(при его отсутствии наберите 0):")
    initialAmount = input()

    def payment(c, y, p, i):
        s = (int(c) - int(i)) * ((float(p) / 100 / 12) + (
                    (float(p) / 100 / 12) / ((1 + (float(p) / 100 / 12)) ** (int(y)) - 1)))
        print("Ежемесячный платеж равен:", round(s, 2))
        print("Общая сумма выплат составит:", int(s*int(y)))
        print("Переплата составит:", (s*int(y))-int(c))

    payment(creditAmount, yearAmount, percent, initialAmount)

def differentiare():
    print("Введите сумму кредита:")
    creditAmount = input()
    print("Введите количество лет:")
    yearAmount = input()
    print("Введите процентную ставку:")
    percent = input()
    print("Введите первоначальный взнос(при его отсутствии наберите 0):")
    initialAmount = input()

    def payment(c, y, p, i):
        d =int((int(c) - int(i)) / (float(y) * 12))
        print("Ежемясячный платеж по основному долгу:", d)
        month = float(y) * 12
        r=0
        for i in range(1, int(month)+1):
            z = d+(((int(c) - int(i)) - d * (int(i) - 1)) * (float(p) / 100 / 12));
            print("Месяц: ", i, " ежемесячный платеж ", int(z), " ", " из них процентов: ", (int(z)-d))
            r =int(r)+int(z)
            if i == int(month):
                print("Общая сумма выплат: ",r)
    payment(creditAmount, yearAmount, percent, initialAmount)

if(change == "1"):
    annuitet()
elif(change == "2"):
    differentiare()
else:
    print("Такого платежа нет. Программа закончена")





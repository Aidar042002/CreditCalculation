print("Программа для расчета аннуитетного и дифференцированного платежей")

print("Введите вид платежа 1(an) или 2(dif)")
change = input()


creditAmount =0
yearAmount = 0
percent = 0
initialAmount = 0

def annuitet():
    print("Введите сумму кредита:")
    creditAmount = input()
    print("Введите количество лет:")
    yearAmount = input()
    print("Введите процентную ставку:")
    percent = input()
    print("Введите первоначальный взнос(при его отсутствии наберите 0):")
    initialAmount = input()

    def payment(c, y, p, i):
        s = (int(c) - int(i)) * ((float(p) / 100 / 12) + (
                    (float(p) / 100 / 12) / ((1 + (float(p) / 100 / 12)) ** (int(y) * 12) - 1)))
        print("Ежемесячный платеж равен:", round(s, 2))

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

    def payment(creditAmount, yearAmount, percent, initialAmount):
        d =int((int(creditAmount)-int(initialAmount))/(float(yearAmount)*12))
        print("Ежемясячный платеж по основному долгу:", d)
        month = float(yearAmount) *12
        for i in range(1, int(month)+1):
            z = d+(((int(creditAmount)-int(initialAmount))-d*(int(i)-1))*(float(percent)/100/12));
            print("Месяц: ", i, " ежемесячный платеж ", int(z), " ", " из них процентов: ", (int(z)-d))
    payment(creditAmount, yearAmount, percent, initialAmount)

if(change == "1"):
    annuitet()
elif(change == "2"):
    differentiare()
else:
    print("Такого платежа нет. Программа закончена")





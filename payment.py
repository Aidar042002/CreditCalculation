print("Программа для расчета аннуитетного и дифференцированного платежей")
print("Введите сумму кредита:")
creditAmount = input()
print("Введите количество лет:")
yearAmount = input()
print("Введите процентную ставку:")
percent = input()
print("Введите первоначальный взнос(при его отсутствии наберите 0):")
initialAmount = input()

def payment(c, y, p, i):
    s = (int(c) - int(i)) * ((float(p) / 100 / 12) + ((float(p) / 100 / 12) / ((1 + (float(p) / 100 / 12)) ** (int(y) * 12) - 1)))
    print("Ежемесячный платеж равен:", round(s, 2))
payment(creditAmount, yearAmount, percent, initialAmount)
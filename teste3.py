income = float(input("Entre com os rendimentos anuais "))

if income < 85528:
 tax = income * 0.18 - 556.02
elif income > 85528:
 tax = int(income - 85528) * 0.32 + 14389.02

tax = round(tax, 0)
print("A taxa é:", tax, "thalers") 
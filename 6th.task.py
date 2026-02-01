import math
def unit_price(diameter_cm, price_euro):
    radius_m =(diameter_cm / 2)/ 100
    area = math.pi * radius_m ** 2
    return price_euro / area

# Main program
d1 = float(input("enter diameter of pizza 1 (cm):"))
p1 = float(input("enter price of pizza 1 (euro:"))

d2 = float(input("enter diameter of pizza 2 (cm):"))
p2 = float(input("enter price of pizza 2 (euro):"))

price1 = unit_price(d1, p1)
price2 = unit_price(d2, p2)

print(f"pizza 1 unit price: {price1:.2f} €/m²")
print(f"pizza 2 unit price: {price2:>2f}€/m²")

if price1 < price2:
    print("pizza 1 provides better value for money.")
elif price2 < price1:
    print("pizza 2 provides better value for money.")
else:
    print("Both pizzas have same value of money.")
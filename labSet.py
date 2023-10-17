nestleProduct = {
    "KitKat": 34456432,
    "Nescafe": 14106132,
    "Maggi": 9960312,
    "Nido": 44506003
}

unileverProduct = {
    "Lipton": 23456000,
    "Breyers": 1235891,
    "HellManns": 17241412,
    "Marmite": 11715324
}

nestleCountries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unileverCountries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(f"product sales of nestle:")
for product, sales in nestleProduct.items():
    print(f"{product}: {sales} US Dollars")

print("\n")

print(f"product sales of unilever:")
for product, sales in unileverProduct.items():
    print(f"{product}: {sales} US Dollars")

print("\n")

if len(nestleProduct) > len(unileverProduct):
    print("Nestle more products")
elif len(nestleProduct) < len(unileverProduct):
    print("Unilever more products")
else:
    print("Nestle and Unilever equal number of products")

print("\n")

maxValueNestle = max(nestleProduct , key=nestleProduct.get)
print("Top selling product for nestle:")
print(f"{maxValueNestle}: {nestleProduct[maxValueNestle]} US Dollars")

print("\n")

maxValueUnilever = max(unileverProduct, key=unileverProduct.get)
print("Top selling product for unilever:")
print(f"{maxValueUnilever}: {unileverProduct[maxValueUnilever]} US Dollars")

print("\n")

print("Countries where Nestle is sell:")
for Countries in nestleCountries:
    print(Countries)

print("\n")

print("Countries where Unilever is sell:")
for Countries in unileverCountries:
    print(Countries)

print("\n")

commonCountries = nestleCountries.intersection(unileverCountries)
print("Countries where Nestl and Unilever sell their products:")
for Countries in commonCountries:
    print(Countries)

print("\n")

nestleCountries1 = nestleCountries.difference(unileverCountries)
print("Countries where Nestle sells but Unilever doesn't:")
for Countries in nestleCountries1:
    print(Countries)

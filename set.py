empty_dict = {}
empty_dict = dict()

nestle_product = {
    "KitKat": 34456432 ,
    "Nescafe": 14106132,
    "Maggi": 9960312,
    "Nido": 44506003
}

unilever_product = {
    "Lipton": 23456000,
    "Breyers": 1235891,
    "HellManns": 17241412,
    "Marmite": 11715324
}

for product, sales in nestle_product():
    print(f"{product}: {sales} US Dollars")

print(nestle_product)
print("nestle products and sales figures:")
print(len(nestle_product))

print("Unilever Products:")
for product, sales in unilever_product():
    print(f"{product}: {sales} US Dollars")
    
print(unilever_product)
print("Unilever products and sales figures:")
print(len(unilever_product))


empty_set = set()
countries_nestle_sell = {"Saudi Arabia", "Oman","Kuwait","Egypt", "Jordan", "Sudan"}
print(countries_nestle_sell)

countries_unilever_sell = {"Saudi Arabia","Kuwait","Iraq","Morocco", "Yemen","United Emirates"}
print(countries_unilever_sell)

number_nestle_prodect = len(nestle_product)
number_unilever_product = len(unilever_product)

if number_nestle_prodect > number_unilever_product:
 print("nestle product is more than unilever product")

elif number_nestle_prodect < number_unilever_product:
 print("tunilever product is more than nestle produc")

else:
  number_nestle_prodect = number_unilever_product
print("tunilever product is equal nestle produc")


top_nestle_product=max(nestle_product,key=nestle_product.get)
print(f"{top_nestle_product}")

top_unilever_product=max(unilever_product,key=unilever_product.get)
print(f"{top_unilever_product}")

if "Saudi Arabia & Oman & Kuwait & Egypt & Jordan & Sudan" in countries_nestle_sell:
 print ("this city Nestle sell their products")

if "Saudi Arabia & Kuwait & Iraq & Morocco & Yemen & United Emirates" in countries_unilever_sell:
 print ("this city Unilever sell their products")

nestle_unilver_intersection = countries_nestle_sell.intersection( countries_unilever_sell)
print ("nestle unilver intersection",nestle_unilver_intersection)

nestle_unilver_defference = countries_nestle_sell - countries_unilever_sell
print("Nestle, Unilver Differenc", nestle_unilver_defference)

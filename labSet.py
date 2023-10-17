print("_"*50)

Nestle_products={"KitKat":34456432,
                 "Nescafe":14106132,
                 "Maggi":9960312,
                 "Nido":44506003
                 }
Unilever_products={
    "Lipton": 23456000, 
    "Breyers" : 1235891,
    "HellManns" : 17241412
    ,"Marmite":11715324
    }

print(Nestle_products)
print(Unilever_products)

Nestle_countries= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_countries={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("_"*50)

if len(Nestle_products)> len(Unilever_products):
    print("The Nestle products more then Unilever products ")
elif len(Nestle_products)<len(Unilever_products):
     print("The Unilever products more then Nestle products ")
else:
     print("The number Unilever products is equal number Nestle products")  

print("_"*50)

top_selling_Nestle=max(Nestle_products,key=Nestle_products.get)
print(f"Top selling product from Nestle is {top_selling_Nestle}:{Nestle_products[top_selling_Nestle]} US Dollars")

print("_"*50)

top_selling_Unilever=max(Unilever_products,key=Unilever_products.get)
print(f"Top selling product from Unilever is {top_selling_Unilever}:{Unilever_products[top_selling_Unilever]} US Dollars")

print("_"*50)

for city_Nestle in Nestle_countries:
    print(f"The cities Nestle sell their products : {city_Nestle}")
print("_"*50)
for city_Unilever in Unilever_countries:
    print(f"The cities Unilever sell their products : {city_Unilever}")

print("_"*50)
Both_city=Nestle_countries & Unilever_countries

for city in Both_city:
    print(f"The cities that both Nestle & Unilver sell in common: {city}")

print("_"*50)

Diffr_city= Nestle_countries - Unilever_countries
for city in Diffr_city:
    print(f"The cities Nestle sells in , but Unilver doens't sell in: {city}")

print("_"*50)
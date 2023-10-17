#1
nestle_products = {
    "KitKat":34456432,
    "Nescafe":14106132,
    "Maggi":9960312,
    "Nido":44506003 
}
#2
unilever_products = {
    "Lipton":23456000,
    "Breyers":1235891,
    "HellManns":17241412,
    "Marmite":11715324 
}

nestle_sells_country = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
}
unilever_sells_country = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#3
print("----Nestle----")
counter1 = 0
for name,price in nestle_products.items():
    print(f"Products name: {name} and the total number of sells {price} US Dollars")
    counter1 += 1
#4
print("----Unilever----")
counter2 = 0
for name,price in unilever_products.items():
    print(f"Products name: {name} and the total number of sells {price} US Dollars")
    counter2 += 1
#5
print("#"*29)
print(f"Nestle have {counter1} product and Unilever have {counter2} product, Nestle have {counter1 - counter2} more product than Unilever and Unilever have { counter2 - counter1} more product than Nestle")
print("#"*29)

best_sales_unilever = 0
best_product_unilever_name = ""
for product in unilever_products:
    if unilever_products[product] > best_sales_unilever:
        best_sales_unilever = unilever_products[product]
        best_product_unilever_name = product 
print(f"The best selling product in Unilever is : {best_product_unilever_name} its sales {best_sales_unilever}")

best_sales_nestle = 0
best_product_nestle_name = ""
for product in nestle_products:
    if nestle_products[product] > best_sales_nestle:
        best_sales_nestle = nestle_products[product]
        best_product_nestle_name = product
print(f"The best selling product in Unilever is : {best_product_nestle_name} its sales {best_sales_nestle}")
print("#"*29)
for city in nestle_sells_country:
    print(f"Nestle selling product in {city}")
for city in unilever_sells_country:
    print(f"Univlever selling product in {city}")
print("#"*29)
print("----Both sells in the same country----")
both_have_same_country = nestle_sells_country.intersection(unilever_sells_country)
for country in both_have_same_country:
    print(country)
print("----Nestle sells in country that Unilever's don't----")
nestle_sells_more_than_unilever = nestle_sells_country - unilever_sells_country
for country in nestle_sells_more_than_unilever:
    print(country)

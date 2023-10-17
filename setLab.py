#1
nestle_products = {
    "KitKat":34456432,
    "Nescafe":14106132,
    "Maggi":9960312 ,
    "Nido":44506003 
}
#2
unilever_products = {
    "Lipton":23456000,
    "Breyers":1235891,
    "HellManns":17241412  ,
    "Marmite":11715324 
}

Nestle_sells_country = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
}
Unilever_sells_country = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("----Nestle----")
for name,price in nestle_products.items():
    print(f"Products name: {name} and the total number of sells {price} US Dollars")
print("----Unilever----")
for name,price in unilever_products.items():
    print(f"Products name: {name} and the total number of sells {price} US Dollars")

print("#"*29)

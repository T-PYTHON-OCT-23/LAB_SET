nestle_products={
    "KitKat" : 34456432 ,
    "Nescafe": 14106132,
    "Maggi" : 9960312,
    "Nido": 44506003,

     }

unilever_products ={
    "Lipton":23456000 ,
    "Breyers" :1235891,
    "HellManns" :17241412,
    "Marmite" :11715324
}
#Nestle Products
print("Nestle Products")
each_product_sold1 = [i for i in nestle_products.items()]
print(each_product_sold1)

print("-"*20)
#Unilever Products
print("Unilever Products")
each_product_sold2 = [n for n in unilever_products.items()]
print(each_product_sold2)

print("-"*20)

nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#Print which of the companies has more products that the other company.
print("-"*20)
print("Which of the companies has more products that the other company")
val1 = len(nestle_products)
val2 = len(unilever_products)
if val1 == val2:
    print("Neither company has more products than the other.")

print("-"*20)
#The Top selling 

top_selling_nestle = {k:v for k,v in nestle_products.items() if max(nestle_products.values()) == v }
print("the top selling product from Nestle", top_selling_nestle)


top_selling_unilever = {k:v for k,v in unilever_products.items() if max(unilever_products.values()) == v }
print("the top selling product from Unilever", top_selling_unilever)

#Sets
print("-"*20)
value1 = nestle_cities | unilever_cities
print("All the cities Unilever & Nestle sell their products in : \n" ,value1)
value2 = nestle_cities & unilever_cities
print("the cities that both Nestle & Unilver sell in common : \n", value2)
value3 = nestle_cities - unilever_cities
print("the cities Nestle sells in , but Unilver doens't sell in : \n", value3)


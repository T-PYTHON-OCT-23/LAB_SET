nestle_products = {
    "KitKat" : 34456432 ,
    "Nescafe" : 14106132 ,
    "Maggi" : 9960312 ,
    "Nido" : 44506003 
}
unilever_products = {
    "Lipton" : 23456000 ,
    "Breyers" : 1235891 ,
    "HellManns" : 17241412 ,
    "Marmite" : 11715324
}

nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("-----Nestle-----")
for product in nestle_products :
    print(f"the product: {product} , and the sales: {nestle_products[product]} US Dollars")
print("-----Unilever-----")
for product in unilever_products :
    print(f"the product: {product} , and the sales: {unilever_products[product]} US Dollars")

counter_nestle_products =0 
for product in nestle_products :
    counter_nestle_products += 1
    
counter_unilever_products =0 
for product in unilever_products :
    counter_unilever_products += 1
   
print("\n----The company with the most products----") 

if counter_nestle_products > counter_unilever_products :
    print("Nestle has more products than Unilever .")
elif counter_nestle_products < counter_unilever_products:
    print("Unilever has more products than Nestle .")
else:
    print("The products of both companies are equal")
    
print("\n----Best selling product----")
best_sales_nestle = 0
best_product_nestle = ""
for product in nestle_products:
    if nestle_products[product] > best_sales_nestle:
        best_sales_nestle = nestle_products[product]
        best_product_nestle = product 
print(f"the best selling product in Nestle is : {best_product_nestle} its sales {best_sales_nestle}")
     
best_sales_unilever = 0
best_product_unilever = ""
for product in unilever_products:
    if unilever_products[product] > best_sales_unilever:
        best_sales_unilever = unilever_products[product]
        best_product_unilever = product 
print(f"the best selling product in Unilever is : {best_product_unilever} its sales {best_sales_unilever}")

print("\n---the cities Unilever & Nestle sell their products in---")
print("\nthe cities Nestle sell their products in : ")
for city in nestle:
    print(city)
print("\nthe cities Unilever sell their products in : ") 
for city in unilever:
    print(city)
    
print("\n --- the cities that both Nestle & Unilver sell in common---")
union_citys = nestle | unilever
for city in union_citys:
    print(city)

print("\n --- the cities Nestle sells in , but Unilver doens't sell in---")
nestle_difference = nestle - unilever
for city in nestle_difference:
    print(city)   

        
        
    





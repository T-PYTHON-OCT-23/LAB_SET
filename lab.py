nestle_products={
 "KitKat" :   34456432 ,
 "Nescafe"   :14106132 ,
 "Maggi"     : 9960312,
 "Nido"      : 44506003
}
unilever_products={
 "Lipton"    : 23456000 ,
 "Breyers"   : 1235891,
 "HellManns" : 17241412,
 "Marmite"   : 11715324 
}
Nestle ={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"} 


print('Products for Nestle company:')
for key, value in nestle_products.items():
    print(key, value)
print('---'*20)
print('Products for Unilever company:')
for key, value in unilever_products.items():
    print(key, value)


top_selling_product_Nestle=max(nestle_products,key=nestle_products.get)
print(f"The top selling product from Nestle is {top_selling_product_Nestle} whit sales of {nestle_products[top_selling_product_Nestle]}")


top_selling_product_unilever=max(unilever_products,key=unilever_products.get)
print(f"The top selling product from Nestle is {top_selling_product_unilever} whit sales of {unilever_products[top_selling_product_unilever]}")

if len(nestle_products)> len(unilever_products):
    print('Nestle has more products')
elif len(nestle_products) < len(unilever_products):
    print('Unilever has more products.')
else :
    print('The companies are equal in prouducts')

union_unilever_and_Nestle=Nestle|Unilever
print('All the cities Unilever & Nestle sell their products in')
for i in union_unilever_and_Nestle:
    print(i)

intersection_unilever_and_Nestle=Nestle&Unilever
print('The cities that both Nestle & Unilver sell in common')
for i in intersection_unilever_and_Nestle:
    print(i)
print("The cities Nestle sells in , but Unilver doens't sell in")
difference_unilever_and_Nestle=Nestle-Unilever
for i in difference_unilever_and_Nestle:
    print(i)





    







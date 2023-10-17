Nestle_product={
 "KitKat" : 34456432 ,
 "Nescafe" : 14106132 ,
 "Maggi" : 9960312 ,
 "Nido" : 44506003 
}


Unilever_product={
 "Lipton" : 23456000 ,
 "Breyers" : 1235891 ,
 "HellManns" : 17241412 ,
 "Marmite" : 11715324 
}


Nestle= {
     "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
}

Unilever = {
    "Saudi Arabia", "Kuwait", "Iraq",
    "Morocco", "Yemen", "United Emirates"
}

print("Unilever products: ")
for i in Unilever_product:
    print(i, Unilever_product[i])   
print("Nestle products: ")
for i in Nestle_product:
    print(i, Nestle_product[i])   

if len(Nestle_product)>len(Unilever_product):
    print("Nestle has more products")
    

if len(Nestle_product)<len(Unilever_product):
    print("Unilever has more products")
    
else:
    print("Nestle and Unilever have the same number of products")
    
print("Nestle highest selling product:")
high_value=(max(Nestle_product.values()))
index_=[list(Nestle_product.values()).index(high_value)]
print(list(Nestle_product.keys())[index_[0]],high_value)


   
print("Unilever highest selling product:")
high_value=(max(Unilever_product.values()))
index_=[list(Unilever_product.values()).index(high_value)]
print(list(Unilever_product.keys())[index_[0]],high_value)


print("Nestle and Unilever countries:")

for i in Nestle.union(Unilever):
    print(i,end=" ")

print("\nNestle and Unilever difference countries:")
for i in Nestle.difference(Unilever):
    print(i,end=" ")
    

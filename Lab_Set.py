Nestle_products = {"KitKat" : 34456432 ,
"Nescafe" : 14106132 ,
 "Maggi" : 9960312 ,
 "Nido" : 44506003 }
Unilever_products={ "Lipton" : 23456000,
 "Breyers" : 1235891 ,
 "HellManns" : 17241412,
 "Marmite ":11715324}
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("________Welcome________")
for key,value in Nestle_products.items():
    print(key,value)
print("___________________________________________________________")
for key,value in Unilever_products.items():    
    print(key,value)
for i in Nestle_products:
    len(i)
for j in Unilever_products:
    len(j)
print("___________________________________________________________")    
if len(i)>len(j):
    print("Nestle_products")  
    print("___________________________________________________________")
else:
    print("the company has more products: they equal")  
      
for key,value in Nestle_products.items():
    list_value = [value]
    max(list_value)
print("___________________________________________________________")
print("the top selling product from Nestle: ")    
print(key,value) 
for key,value in Unilever_products.items():
    list_value = [value]
    max(list_value)
print("___________________________________________________________") 
print("the top selling product from Unilever: ")   
print(key,value) 
print("___________________________________________________________")
print("the cities Unilever & Nestle sell their products in: ")
for city in Nestle | Unilever:
    print(city)    
print("___________________________________________________________")
print("the cities that both Nestle & Unilver sell in common: ")    
for city in Nestle & Unilever:
    print(city) 
print("___________________________________________________________")
print("the cities Nestle sells in , but Unilver doens't sell in")
for city in Nestle - Unilever:
    print(city)       
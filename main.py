nestle_products ={
     " KitKat": 34456432 ,
        " Nescafe": 14106132 , 
        " Maggi" :  9_960_312  ,
         " Nido" : 44506003  }

unilever_product = {
      " Lipton": 23456000 ,
          " Breyers": 1235891 , 
        " HellManns" :  17241412, 
        " Marmite" : 11715324   }

# Print each product sold by nestle and the sales figures / numbers  for that product.
for key , value in nestle_products.items():
    print(f"{key , value}US Dollars")
print()
# Print each product sold by Unilever and the sales figures / numbers  for that product.
for key , value in unilever_product.items():
    print(f"{key , value}US Dollars")

print()

#Print which of the companies has more products that the other company.
if len(unilever_product) > len(nestle_products):
    print("unilever company has more products") 
elif len(unilever_product) < len(nestle_products):
    print("Nestle company has more products") 
else:
      print("nestle and unilever company has equal products")

print()
#- Print the top selling product from Nestle with sales figures.
top_nes= max(nestle_products, key=nestle_products.get)
print(f"The top selling products is {top_nes} with a score of {nestle_products[top_nes]}US Dollars.")

print()

# Print the top selling product from Unilever with sales figures.
top_uni= max(unilever_product, key=unilever_product.get)
print(f"The top selling products is {top_uni} with a score of {unilever_product[top_uni]}US Dollars.")

print()
nes_city = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"  }
uni_city ={ "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates" }

# print all the cities Unilever & Nestle sell their products in
print( nes_city | uni_city )

print()

#print the cities that both Nestle & Unilver sell in common.
print( nes_city & uni_city )

print()

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in'''
print ( nes_city  - uni_city )
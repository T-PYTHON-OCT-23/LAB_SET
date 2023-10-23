
#Create a variable to hold the values of Nestle products (use a dicitionary)
nestle_products = {
"KitKat" : 34_456_432,
"Nescafe" : 14_106_132,
"Maggi" : 9_960_312,
"Nido" : 44_506_003

}

#Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_products={
"Lipton" : 23_456_000,
"Breyers" : 1_235_891,
"HellManns" : 17_241_412,
"Marmite" : 11_715_324
}


print("Nestle Products and Sales:")
#Print each product sold by Unilever and the sales figures / numbers  for that product
for unilever_key, unilever_value in unilever_products.items():
    print(f"{unilever_key}: {unilever_value}")

for nestle_key, nestle_value in nestle_products.items():
    print(f"{nestle_key}: {nestle_value} ")    

if len(nestle_products) > len(unilever_products):
    print("Nestle has more products than Unilever ")
elif len(nestle_products) < len(unilever_products):
   print("Unilever has more products than Nestle ")
else:
    print("the prodects of Unilever and Nestle are equal")

# Print the top selling product from Nestle with sales figures.
# Print the top selling product from Unilever with sales figures.

print("The top selling product from Nestle is: " , max(nestle_products.items()))

max_keys  = [ (key , value) for key, value in unilever_products.items() if value == max(unilever_products.values())]

print("The top selling product from Unilever is: " , max_keys)

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
cities_nestle= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
cities_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(cities_unilever| cities_nestle)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print(cities_nestle & cities_unilever)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print(cities_nestle - cities_unilever)


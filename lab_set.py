
#Create a variable to hold the values of Nestle products (use a dicitionary)
nestle_products = {
"KitKat" : "34,456,432 US Dollars",
"Nescafe" : "14,106,132 US Dollars",
"Maggi" : "9,960,312 US Dollars",
"Nido" : "44,506,003 US Dollars"

}


#Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_products={
"Lipton" : "23,456,000 US Dollars",
"Breyers" : "1,235,891 US Dollars",
"HellManns" : "17,241,412 US Dollars",
"Marmite" : "11,715,324 US Dollars"
}

#Print each product sold by Unilever and the sales figures / numbers for that product.
for unilever_key , unilever_value in unilever_products.items():
    print(unilever_key , unilever_value)


#Print each product sold by Nestle and the sales figures / numbers for that product.
for nestle_key , nestle_value in nestle_products.items():
    print(nestle_key , nestle_value)


#Print which of the companies has more products that the other company.
length_nestle = len(nestle_products)
#print(length_nestle)

length_unilever = len(unilever_products)
#print(length_unilever)

if length_nestle > length_unilever:
    print(f"the prodects of Nestle are more than Unilever , Nestle have {length_nestle} prodects")
elif length_nestle < length_unilever:
    print(f"the prodects of Unilever are more than Nestle , Unilever have {length_unilever} prodects")
else:
    print("the prodects of Unilever and Nestle are equal")



#Print the top selling product from Nestle with sales figures.
'''
def top_selling_nestle ( nestle_products:dict):
    for i , j in nestle_products.items():
        top_sell_nestle=max(i ,j )
    for i in nestle_products.keys(), nestle_products.values():
        top_sell_nestle += max(i)
    
    return top_sell_nestle 

print("top selling prodect from Nestle is : ",top_selling_nestle(nestle_products))

#Print the top selling product from Unilever with sales figures.
def top_selling_unilever ( unilever_products:dict):
    for i , j in unilever_products.items():
        top_sell_unilever = max(i ,j )
    for i in unilever_products.keys() , unilever_products.values():
        top_sell_unilever += max(i)
    return top_sell_unilever

print("top selling prodect from Unilever is : ",top_selling_unilever(unilever_products))
'''

print("top selling prodect from Nestle is : " , max(nestle_products.items()))
max_keys  = [ (key , value) for key, value in unilever_products.items() if value == max(unilever_products.values())]

print("top selling prodect from Unilever is : " , max_keys)





#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
set_nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
set_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print(set_nestle | set_unilever)


#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print(set_nestle & set_unilever)


#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print(set_nestle - set_unilever)

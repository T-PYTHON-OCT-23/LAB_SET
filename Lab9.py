Nestle_products = {
     "KitKat" : 34456432  ,
     "Nescafe" : "14,106,132 US Dollars" ,
     "Maggi" : "9,960,312 US Dollars" ,
     "Nido" : "44,506,003 US Dollars"
}
print(Nestle_products)

Unilever_products = {
     "Lipton" : "23,456,000 US Dollars" ,
     "Breyers" : "1,235,891 US Dollars" ,
     "HellManns" : "17,241,412 US Dollars" ,
     "Marmite" : "11,715,324 US Dollars"
}
print(Unilever_products)

if len(Nestle_products) > len(Unilever_products) :
    print(f"{Nestle_products} have more products than {Unilever_products} ")
elif len(Nestle_products) < len(Unilever_products) :
    print(f"{Unilever_products} have more products than {Nestle_products} ")
else :
    print("Nestle and Unilever have equle length product ")


print("top selling prodect from Nestle is :" , max(Nestle_products.items () ))
max_keys = [ (key , value) for key, value in Unilever_products.items () if value == max(Unilever_products.values ())]
print ("top selling prodect from Unilever is : " , max_keys)



city_nes = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
city_uni = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates" }
print(city_nes | city_uni)
print(city_nes & city_uni)
print(city_nes - city_uni)



'''
Nestle1 = Nestle_products.get("KitKat")
print(Nestle1)
Nestle2 = Nestle_products.get("Nescafe")
print(Nestle2)
Nestle3 = Nestle_products.get("Maggi")
print(Nestle3)
Nestle4 = Nestle_products.get("Nido")
print(Nestle4)
print("\n")
Unilever1 = Unilever_products.get("Lipton")
print(Unilever1)
Unilever2 = Unilever_products.get("Breyers")
print(Unilever2)
Unilever3 = Unilever_products.get("HellManns")
print(Unilever3)
Unilever4 = Unilever_products.get("Marmite")
print(Unilever4) 
print("\n")
for Nestle1 in Nestle_products :
    if Nestle1 > Nestle2 and Nestle1 > Nestle3 and Nestle1 > Nestle4:
        print(Nestle1)

    elif Nestle2 > Nestle1 and Nestle2 > Nestle3 and Nestle2 > Nestle4:
        print(Nestle2)
    elif Nestle3 > Nestle2 and Nestle3 > Nestle2 and Nestle3 > Nestle4:
        print(Nestle3) 
    else:
        print(Nestle4) 
print("\n")
for Unilever1 in Unilever_products :
    if Unilever1 > Unilever2 and Unilever1 >Unilever3 and Unilever1 >Unilever4:
        print(Unilever1)
    elif Unilever2 > Unilever1 and Unilever2 >Unilever3 and Unilever2 >Unilever4:
        print(Unilever2)
    elif Unilever3 > Unilever1 and Unilever3 >Unilever2 and Unilever3 >Unilever4:
        print(Unilever1)
    else:
        print(Unilever4) 
 '''   


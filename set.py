Nestle={"kitkat":34456432,
        "Nescafe":14106132,
        "Maggi":9960312,
        "Nido":44506003}


Unilever={"Lipton":23456000,
          "Breyers":1235891,
          "HellManns":17241412,
          "Marmite":11715324}

print(Nestle)
print(Unilever)

print("_"*100)
ns = len(Nestle)
un = len(Unilever)
if ns > un:
    print("Nestle has more products")
elif ns<un:
    print("Unilever has more products")
elif ns == un:
    print("The two companies are equal in number of products")

productـn = { key:value for key,value in Nestle.items() 
             if max(Nestle.values())
               == value }
print("The most sold product at Nestlé:", productـn)

product_u = {key:value for key,value in Unilever.items() 
             if max(Unilever.values())
               == value }
print("The most sold product at  Unilever:", product_u)

print("_"*100)

Nestle_a= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever1={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
n= Nestle_a|Unilever1
m= Nestle_a&Unilever1
g=Nestle_a-Unilever1
print(n)
print(m)
print(g)





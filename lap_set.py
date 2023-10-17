Nestle = {"kitkat" : 34456432, "Nescafe" : 14106132, "Maggi" : 9960312, "Nido" : 44506003}
unilever = {"Lipto" : 23456000, "Breyers" : 1235891, "HellManns" : 17241412, "Marmite" :11715324}
nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
for marketN, sale in Nestle.items():
    print(marketN,"   ", sale)
for marketU, saleU in unilever.items():
    print (marketU,"  ", saleU)

if len(Nestle) > len(unilever):
    print("Nestle is BIG")
else:
     print("drow")

top_prodictN = max(Nestle.values())
for prodi , sless in Nestle.items():
    if sless == top_prodictN:
        print (f"top selling product from Nestle" ,prodi, sless)

top_prodictU = max(unilever.values())
for prodictU , slessU in unilever.items():
    if slessU == top_prodictU:
        print (f"top selling product from Unilever" ,prodictU, slessU)

print(f"all the cities Unilever & Nestle sell their products in." , nestle_cities | unilever_cities)
print (f"the cities that both Nestle & Unilver sell in common" ,nestle_cities & unilever_cities)
print (f"the cities Nestle sells in , but Unilver doens't sell in.",nestle_cities - unilever_cities)
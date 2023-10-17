nestleSales = {
    "KitKat" : 34456432     ,
    "Nescafe" : 14106132    ,
    "Maggi" : 9960312       ,
    "Nido" : 44506003
 }
unileverSales = {
    "Lipton" : 23456000     ,
    "Breyers" : 1235891     ,
    "HellManns" : 17241412  ,
    "Marmite" : 11715324
 }

companiesDict={
    "Nestle" : nestleSales,
    "Unilever" : unileverSales
}
def printSales(dictionary:dict):
    for key in dictionary:
        print(f"{key} = {dictionary[key]}")
printSales(nestleSales)
print("--"*20)
printSales(unileverSales)
print("--"*20)

if len(nestleSales)>len(unileverSales):
     print("Nestle has more products than Unilever ")
elif len(nestleSales)<len(unileverSales):
     print("Unilever has more products than Nestle")
else:
     print("both has the same amount of products")
print("--"*20)
print(f"top selling product for Nestle is: {max(nestleSales, key=nestleSales.get)}")
print(f"top selling product for Unilever is: {max(unileverSales, key=unileverSales.get)}")
print("--"*20)

nestleLocations = set({"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"})
unileverLocations = set({"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"})

all_cities=nestleLocations|unileverLocations
print("all cities that Nestle and Unilver sell in  ->",all_cities)
print()
incommon_cities=nestleLocations&unileverLocations
print("in common cities between Nestle and Unilver -> ",incommon_cities)
print()
nestleButNotUnilver=nestleLocations-unileverLocations
print("Nestle sells in, but Unilver doens't sell in -> ", nestleButNotUnilver)
print()
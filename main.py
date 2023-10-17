
kata_Nestle_sales_products = {
    'KitKat' : 34456432,
    'Nescafe': 14106132,
    'Maggi'  : 9960312,
    'Nido'   : 44506003
  
 }

Dalia_Unilever_sales_products = {
    'Lipton' : 23456000,
    'Breyers' : 1235891,
    'HellManns' :17241412,
    'Marmite' : 11715324

}

monica_sell_products={
    'Nestle' : ["Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"],

    'Unilever' : ["Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"]
}


print(Dalia_Unilever_sales_products)

print(kata_Nestle_sales_products)

if len(Dalia_Unilever_sales_products) >  len(kata_Nestle_sales_products):

    print("Dalia companies has more products")
elif len(Dalia_Unilever_sales_products) == len(kata_Nestle_sales_products):
    print("Equle products")
else:print("kate companies has more products")

print("-"*20)

def top_selling_product(company:dict) -> str:
    value_list=[]
    key_list=[]

    for key ,value in company.items():
        value_list.append(value)
        key_list.append(key)

    top_sale=max(value_list)
    top_sale_prodect = key_list[value_list.index(top_sale)]
    return f"{top_sale_prodect} with {top_sale}$"

print(f"the top selling product in Nestle is {top_selling_product(kata_Nestle_sales_products)}")
print(f"the top selling product in Unilever is {top_selling_product(Dalia_Unilever_sales_products)}")

print("-"*20)

Nestle_sold_city= monica_sell_products["Nestle"]
Unilever_sold_city=monica_sell_products["Unilever"]



def show_citis(set:set)->str:

    for city in set:

        print(city)

sold_products_in_city_for_both= set(Nestle_sold_city).union(set(Unilever_sold_city))
print("-"*20)
print("sold products in cities for both:")
show_citis(sold_products_in_city_for_both)

print("-"*20)
coomen_cities= set(Nestle_sold_city).intersection(set(Unilever_sold_city))
print("\ncommon cities:")
show_citis(coomen_cities)
print("-"*20)

Nestle_sells_in= set(Nestle_sold_city).difference(set(Unilever_sold_city))

print("\nthe cities Nestle sells in , but Unilver doens't sell in:")
show_citis(Nestle_sells_in)
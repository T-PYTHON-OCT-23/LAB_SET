Nestle_products ={

"kitkat":34456432 ,
    "nescafe" :14106132,
    "maggy":9960312,
    "Nedo":44506003


}
Unilever_products ={

"Lipton":23456000,
"Breyers":1235891,
"HellManns":17241412,
"Marmite":11715324

}
print(Unilever_products)

print(Nestle_products)
top_selling_product_Nestle= max(Nestle_products.values())
print(    "top selling in Nestle: "    ,top_selling_product_Nestle  "$ dolar") 

top_selling_Unilever_product= max(Unilever_products.values())
print(   f"top TOP selling Unilever :"  ,  top_selling_Unilever_product" $ dolar")


nestle_products ={"kitkat","nescafe","maggy","Nedo"}
unilever_products ={"Lipton","Breyers","HellManns","Marmite"}
print(len(Nestle_products))
print(len(Unilever_products))
countries_Nestle={" saudia aribia" ," Oman" "Kuwait", "Egypt","Sudan"}
countries_Unilever={"saudia aribia","Kuwait","Iraq" ,"Morocco","Yemen","United Emirates"}

common_countries =countries_Nestle.union(countries_Unilever)
for country in common_countries:
       print( "countres pothe sell in:" , country)

       s_countries =countries_Nestle.intersection(countries_Unilever)
for country in s_countries:
          
          print("intersection:",country)
          
          
          
          nestle_countries =countries_Nestle.difference(countries_Unilever)
for x in nestle_countries:
          
             print(x)


  
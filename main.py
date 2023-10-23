# LAB_SET

NestleProducts ={

"Kitkat" :34_456_432,
"Nescafe" :14_106_132,
"Maggi" : 9_960_312,
"Nido" :44_506_003

}#dicitionary Nestle

UnileverProducts={
"Lipton" : 23456000,
"Breyers" : 1235891,
"HellManns" : 17241412,
"Marmite" : 11715324

}#dicitionary Unilever

print("product of Unilever : ")
for UnileverKey , UnileverValue in UnileverProducts.items():
    print(UnileverKey ,"-",UnileverValue)#print 

print("*"*10)
print("product of Nestle : ")
for NestleKey , NestleValue in NestleProducts.items():
    print(NestleKey ,"-",NestleValue)#print 


print("*"*15)

lengthNestle = len(NestleProducts)
lengthUnilever = len(UnileverProducts)

if lengthNestle > lengthUnilever:
    print(f"The prodects of Nestle are more than Unilever , Nestle have {lengthNestle} prodects")
elif lengthNestle < lengthUnilever:
    print(f"The prodects of Unilever are more than Nestle , Unilever have {lengthUnilever} prodects")
else:
    print("the prodects of Unilever and Nestle are equal")


print("*"*15)

NestleeTop=max(NestleProducts)
print("Top selling prodect from Nestle is : ",NestleeTop)

UnileverTop=max(UnileverProducts)
print("Top selling prodect from Unilever is : ",UnileverTop)
print("*"*15)


setNestle = {
    "Saudi Arabia", "Oman",
      "Kuwait", "Egypt", "Jordan", "Sudan"
      }
setUnilever = {
    "Saudi Arabia", "Kuwait", 
    "Iraq", "Morocco", "Yemen", "United Emirates"
    }
print("All :")
print(setNestle | setUnilever)
print("*"*15)
print("Sell both in : ")
print(setNestle & setUnilever)
print("*"*15)
print("Nestle sells in , but Unilver doens't sell in.: ")
print(setNestle - setUnilever)


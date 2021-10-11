a=input("Proqram dilini daxil edin - Choose your program language AZ/EN: ")
if a=="AZ":
    fir=int(input("Birinci ədədi daxil edin:"))
    sec=int(input("İkinci ədədi daxil edin:"))
elif a=="EN":
    fir=int(input("Choose your first number:"))
    sec=int(input("Choose your second number:"))
else:
    print("AZ/EN")



result=fir%sec
print(result)






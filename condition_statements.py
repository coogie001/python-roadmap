bio=int(input("Enter your bio marks :"))
chem=int(input("Enter your chem marks :"))
maths=int(input("Enter your maths marks :"))
kisw=int(input("Enter your kisw marks :"))
eng=int(input("Enter your eng marks :"))
total=bio+chem+maths+kisw+eng
print("your total marks are ",total)
if (total>=400):{
    print("pass","grade A")
}
elif(total>=350):{
    print("average","grade B")
}
elif(total>=280):{
    print("below average","grade C")
}
else:{
    print("fail")
}


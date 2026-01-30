weight=int(input("Enter a weight:"))
height=float(input("Enter a height in meter:"))/100
BMI=weight/(height*height)
print("your BMI is",BMI)
n=1
temp=weight
if(BMI<=18.5):
    for i in range(1,temp):
        temp=temp+1
        new_BMI=temp/(height**2)
        if(new_BMI<=18.5):
            continue
        else:
            w=temp-weight
            print("please gain your wait becaus your BMI is low so you have to increase",w,"kg if you increase your wait your BMI is",new_BMI)
            break
elif(BMI>=24.5):
    for i in range(1,temp):
        temp=temp-1
        new_BMI=temp/(height*height)
        if(new_BMI>=24.5):
            continue
        else:
            w=weight-temp
            print("please loss your wait becaus your BMI is high, so you have to reduce",w,"kg if you reduce your wait your BMI is",new_BMI)
            break
    
else:
    print("your weight is normal")

# weight=int(input("enter a weight"))
# height=int(input("Enter a height"))/100
# bmi=weight/height**2

# w=20*height**2
# if bmi>=0 and bmi<18.5:
#     print("lean")
#     print(f"you have to gain weight : {w-weight}")
# elif bmi>=18.6 and bmi<24.5:
#     print("normal")
# else:
#     print("obesity")
#     print(f"you have to loss weight : {weight-w}")
# BMI-Calculator

weight=int(input("Enter a weight:"))
height=float(input("Enter a height in meter:"))/100
BMI=weight/(height*height)
print("your BMI is",BMI)
# n=1
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

a=int(input("Enter a number "))
b=int(input("Enter a second number "))
opera=int(input("Select which operation you would like to perform: 1.Addition , 2.Subtraction , 3.Multiplication ,4.Division"))
if opera==1:
    c=a+b
    print("The answer is for addition is: ",c)
elif opera==2:
    c=a-b
    print("The answer for subtraction is: ",c)
elif opera==3:
    c=a*b
    print("The answer for multiplication is: ",c)
elif opera==4:
     c=a/b
     print("The answer for division is: ",c)
else:
    print("Incorrect operation")
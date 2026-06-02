#Game for identifying random number
import random
A = random.randint(1,100)
print(A)
i=1 
while(i>0): #While True:
    C = (input("Enter number form 1-100 and guess our number or Q to Quit:  "))
    if(C=="Q"):
        print("You Quit")
        break
    B = int(C)
    if(B==A):
        print("Congratulation You match the Number" , B)
        break
    elif(B<A):
        print("Your number is smaller")
    elif(B>A):
        print("Your number is Greatest")
    else:
        print("Try Again")
        i+=1

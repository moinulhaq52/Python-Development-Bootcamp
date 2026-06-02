#Random Password Generator
import random
import string

n = int(input("Enter lenghth of Password so we generate passwrod for you: "))
charater = string.ascii_letters + string.digits + string.punctuation



password = ""
for i in range(n):
    password =  password + random.choice(charater)

print(password)




#By list Comorehension  [function] for i in range(n)
result = "".join([random.choice(charater) for i in range(n)])  #.join to add string
print(str(result))
    


    
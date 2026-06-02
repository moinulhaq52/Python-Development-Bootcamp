

def add(n1, n2):
    return n1 + n2

def multiply(n1 , n2):
    return n1 * n2

def subtract(n1 , n2):
    return n1 - n2

def divide(n1 , n2):
    return n1 / n2

def calculator():
    ans = 0
    print("MOIN CALCULATOR")
    f_num = int(input("What is the first value: \n"))
    more = "y"
    while more == "y":

        print("+\n-\n*\n/")
        sign = input("Choose the symbol from these: \n")
        s_num = int(input("What is you second value:\n"))
        if sign == '+':
            ans = int(add(f_num,s_num))
        if sign == '-':
            ans = int(subtract(f_num,s_num))
        if sign == '*':
            ans = int(multiply(f_num,s_num))
        if sign == '/':
            ans = int(divide(f_num,s_num))
        print(ans)
        m = input("Can you want more with this answer:\nType 'yes' or 'no':\n").lower()
        if m == "yes":
            f_num = ans
        elif m == "no":
            more = "n"
        else:
            more = "n"
            print("You type wrong word so your answer is:")




    print(ans)
calculator()

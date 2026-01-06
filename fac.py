def print_fac(num):
    #function
    print("the factors of",num,"are:")
    for i in range(1,num +1):
        if num % i == 0:
            print(i)
#input from user
num = int(input("Enter your num to find its factors:"))
#calling function
print_fac(num)
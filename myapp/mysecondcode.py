#this programe check given number PRIME or not

num = 407

#prime numbers are grater than 1

if num > 1:

for i in range(2,num):
     if(num % i) == 0:
        print(num,"is not a prime number")

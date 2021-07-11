# python3
LOOPS

1.Write a program to print “Bright IT Career” ten times using for loop

for i in range(1,11):
   print('Bright IT Career')


2.Write a python program to print 1 to 20 numbers using the while loop.

i=1
while i<=20:
   print(i)
   i+=1

3.Program to equal operator and not equal operators
ex:
    a=10
    b=15
    if a==b:
      print('equal')
    else:
      print('not equal')


4.Write a program to print the odd and even numbers.
  
 for i in range(20):
    if ((i % 2) == 0):
        print(i," is even")
    else:
        print(i," is odd")
        
5.Write a program to print largest number among three numbers.

a=10
b=20
c=5
if a > b and a > c:
   print('a is greater')
elif b > c:
   print('b is greater')
else:
   print('c is greater')


6.Write a program to print even number between 10 and 100 using while

x = int(input("Enter a number:"))
i = 1
while i <= x:
    if i % 2 == 0:
        print("Number is even:", i)
    i = i + 1
    
    
7.Write a program to print 1 to 10 using the do-while loop statement.

* In Python programming language, there is no such loop i.e. python does not have a do while loop that can validate the test condition after executing the loop statement. But, we can implement a similar approach like a do while loop using while loop by checking using True instead of a test condition and test condition can be placed in the loop statement, and break the loop's execution using break statement – if the test condition is not true.

count = 1

while True:
    print(count)
    count += 1
    if count>10:
        break



8.program to find Armstrong number or not

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



9.Write a program to find the prime or not.

number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")
    
    
    
10.Write a program to palindrome or not.

Num = int(input("Enter a value:"))  
Temp = num  
Rev = 0  
while(num > 0):  
    dig = num % 10  
    revrev = rev * 10 + dig  
    numnum = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  
    


11.Program for multiple if else statement(Largest number in 10,20 and 30)

numOne=10
numTwo=20
numThr=30
if numOne>numTwo:
    if numTwo>numThr:
        large = numOne
    else:
        if numThr>numOne:
            large = numThr
        else:
            large = numOne
else:
    if numTwo>numThr:
        large = numTwo
    else:
        large = numThr

print("\nLargest Number =", large)

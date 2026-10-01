print("\ntask1 program 1 sum of 2 numbers")
a = 10
b = 20

sum = a + b

print("Sum of", a, "and", b, "=", sum)
#----------------------------------------------------------------
print("\ntask1 program 2 odd or even")
c = 7

if c % 2 == 0:
    print(c, "is Even")
else:
    print(c, "is Odd")
#----------------------------------
print("\ntask1 program 3 factorial")
d = 5

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print("Factorial of", d, "=", fact(d))
#----------------------------------------------------------------
print("\ntask1 program 4 fibonacci sequence")
e = 7

a = 0
b = 1

print("Fibonacci of", e, "terms is:")

for i in range(e):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#----------------------------------------------------------------
print("\ntask1 program 5 string reversal")
f = "hello"

rev = f[::-1]

print("Reverse of", f, "=", rev)
#----------------------------------------------------------------
print("\ntask1 program 6 palindrome")

g = "madam"

if g == g[::-1]:
    print(g, "is Palindrome")
else:
    print(g, "is Not Palindrome")
#----------------------------------------------------------------
print("\ntask1 program 7 leap year")
h = 2024

if h % 400 == 0 or h % 4 == 0 and h % 100 != 0:
    print(h, "is a Leap Year")
else:
    print(h, "is Not a Leap Year")
#----------------------------------------------------------------
print("\ntask1 program 8  armstrong number")
i = 153

s = 0
n = i

while n > 0:
    r = n % 10
    s = s + r ** 3
    n = n // 10

if s == i:
    print(i, "is Armstrong")
else:
    print(i, "is Not Armstrong")
#----------------------------------------------------------------

















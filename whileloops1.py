# 1. Print Numbers from 1 to n

n=int(input("Enter n value:"))
i=1
while i<=n:
    print(i)
    i+=1

# OUTPUT:

# Enter n value:8
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8


# 2. Print Numbers from m to n

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

while m<=n:
    print(m)
    m+=1

# OUTPUT:
# Enter m value:2
# Enter n value:6
# 2
# 3
# 4
# 5
# 6

# 3. Print Numbers from n to 1 in Reverse

n=int(input("Enter n value:"))
i=1
while i<=n:
    print(n)
    n-=1

# OUTPUT:
# Enter n value:4
# 4
# 3
# 2
# 1

#4. Print Numbers from n to m in Reverse

n=int(input("Enter n value:"))
m=int(input("Enter m value:"))

while m>=n:
    print(m)
    m-=1

# OUTPUT:
# Enter n value:2
# Enter m value:6
# 6
# 5
# 4
# 3
# 2

# 5. Sum of n Natural Numbers

n=int(input("Enter n value:"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

# OUTPUT:
# Enter n value:4
# 10

# 6. Factorial of a Number

n=int(input("Enter n value:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)

# OUTPUT:
# Enter n value:5
# 120

# 7. Sum of m to n Numbers

m= int(input("Enter m value:"))
n=int(input("Enter n value:"))

sum=0
while m<=n:
    sum+=m
    m+=1
print(sum)

# OUTPUT:
# Enter m value:2
# Enter n value:5
# 14

# 8. Product of m to n Numbers

m= int(input("Enter m value:"))
n=int(input("Enter n value:"))

prod=1
while m<=n:
    prod*=m
    m+=1
print(prod)

# OUTPUT:
# Enter m value:2
# Enter n value:5
# 120

# 9. Print Factors of a Number

n=int(input("Enter n value:"))

i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1

# OUTPUT:
# Enter n value:6
# 1
# 2
# 3

# 10. Count factors of a nummber

n=int(input("Enter n value:"))
count=0
i=1
while i<=n:
    if n%i==0:  
        count+=1
    i+=1
print(count)

# OUTPUT:
# Enter n value:8
# 4

# 11. Prime Number Check

n=int(input("Enter n value:"))
count=0
i=1
while i<=n:
    if n%i==0:  
        count+=1
    i+=1
if count==2:
    print("Prime number")
else:
    print("Not a prime number")

# OUTPUT:
# Enter n value:7
# Prime number

# 12. Even Numbers from m to n

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

while m<=n:
    if m%2==0:
        print(m)
    m+=1

# OUTPUT:
# Enter m value:2
# Enter n value:9
# 2
# 4
# 6
# 8

# 13. Odd Numbers from m to n

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

while m<=n:
    if m%2!=0:
        print(m)
    m+=1

# OUTPUT:
# Enter m value:3
# Enter n value:9
# 3
# 5
# 7
# 9


# 14. Count of Even and Odd Numbers


m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
even_count=0
odd_count=0

while m<=n:
    if m%2==0:
        even_count+=1
    else:
        odd_count+=1
    m+=1

print("Even count:",even_count)
print("Odd count:",odd_count)

# OUTPUT:
# Enter m value:3
# Enter n value:16
# Even count: 7
# Odd count: 7
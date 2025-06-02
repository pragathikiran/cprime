print("find out all the prime numbers")
n = int(input("enter a number"))

prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2,int(n**0.5) + 1):
    if prime[i]:
        for j in range(i**i,n+1,i):
            prime[j] = False

print("prime numbers upto")
for i in range(n+1):
    if prime[i]:
        print(i,end="")
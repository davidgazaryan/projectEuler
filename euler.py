#1) Find sum of all multiples of 3 or 5 below 1000

def q1():
    count = 0

    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            count += num 

    return count 


#20) find sum of all digits in 100!

def q20(n):
    count = n 
    ans = 0
    for i in range(n-1,0,-1):
        count *= i 

    count = str(count)
    for i in count:
        ans += int(i)
    
    return ans



#4) find largest palindrome from product of two 3 digit numbers

def q4():
    i = 500
    j = 500
    maxAns = 250000

    maxI = 500
    maxJ = 500

    for i in range(500,999):
        for j in range(i,999):
            ans = str(i * j)
            
            if ans == ans[::-1] and int(ans) > maxAns:
                maxI,maxJ,maxAns = i, j, int(ans)

    return maxI,maxJ

print(q4())

#Sum of the digits of number 2 ^ 1000
def q16():
    num = 2 ** 1000
    count = 0

    for i in str(num):
        count += int(i)
    return count 

print(q16())

#Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

def q6():
    sumSquares = 0
    squareSums = 0

    for i in range(1,101):
        sumSquares += i ** 2
        squareSums += i 
    
    squareSums = squareSums **2 

    return squareSums - sumSquares 

print(q6())
    
#What is the smallest positive number that is evenly 
# ivisible by all of the numbers from 1-20
def q5():
    count = 5000
    while True:
        if all(count % i == 0 for i in range(1,21)):
            return count
        count += 20
    
# print(q5())

#find sum of even values in fibonacci sequence for values < 4,000,000

def q2():
    dp = [0] * 50
    dp[1] = 1 
    for i in range(2,50):
        dp[i] = dp[i-1] + dp[i-2]
        if dp[i] >= 4_000_000:
            return sum(el for el in dp if el % 2 == 0)
            
print(q2())
        

def q12():

    n = 1

    while True:
        if n % 2 == 0:
            d = divisor_count(n//2) * divisor_count(n+1)
        else:
            d = divisor_count(n) * divisor_count((n+1)//2)

        if d > 500:
            print(n*(n+1)//2)
            break

        n += 1

def q366(N=10**18):
    import math

    phi = (1 + 5**0.5) / 2
    phi2 = phi * phi

    total = 0
    k = 1

    while True:
        x = int(k * phi2)
        if x > N:
            break
        total += x
        k += 1

    return total


print(q366())


def q50(limit=1_000_000):

    sieve = [True] * limit
    sieve[0:2] = [False, False]
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    prime_set = set(primes)
    
    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)
    
    max_length = 0
    result = 0
    
    for i in range(len(prefix)):
        for j in range(i - max_length - 1):
            current_sum = prefix[i] - prefix[j]
            if current_sum >= limit:
                break
            if current_sum in prime_set:
                max_length = i - j
                result = current_sum
    
    return result, max_length


print(q50())



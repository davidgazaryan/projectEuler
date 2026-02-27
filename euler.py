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

def q16():
    num = 2 ** 1000
    count = 0

    for i in str(num):
        count += int(i)
    return count 

print(q16())


def q30(n):
    count = 0
    





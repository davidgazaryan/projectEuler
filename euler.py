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


def q30(n):
    count = 0

    





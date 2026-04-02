# Write your solution here
def factorials(n: int):
    d = {}
    j = 1
    for i in range(1,n+1):
        d[i]=i*j
        j *= i 
    return d
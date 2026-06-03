# Write your solution here

def prime_numbers():
    number = 2
    value = True
    while True :
        try:
            for i in range(2,number - 1):
                if number % i == 0:
                    value = False
                    break
                elif number % i != 0:
                    value = True
        except:
            yield number
        if value :
            yield number
        number +=  1
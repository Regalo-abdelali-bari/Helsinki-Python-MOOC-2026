def smallest_average(person1: dict, person2: dict, person3: dict):
    averge1 = 0
    averge2 = 0
    averge3 = 0
    for key,num in person1.items():
        if key == "name":
            continue
        
        averge1 += num
    averge1 /= len(person1)
    for key,num in person2.items():
        if key == "name":
            continue
        averge2 += num
    averge2 /= len(person2)
    for key,num in person3.items():
        if key == "name":
            continue
        averge3 += num
    averge3 /= len(person3)
    if averge1 < averge2 and averge1 < averge3 :
        return person1
    elif averge2 < averge1 and averge2 < averge3:
        return person2
    return person3

def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)
print(minmax([3,4,5,6,2,1,3,20,4,5,5,5,2,1,1,-19]))

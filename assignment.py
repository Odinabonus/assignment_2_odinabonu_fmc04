def classify(value):
    if value < 78:
        return "Below range"
    elif value > 82:
        return "Above range"
    else:
        return "In range"
    
def calculate_average(total , count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result 

count =int(input("Enter the number of ribbons : "))

total = 0
below_range = 0
in_range = 0
above_range = 0

for i in range(count):
    length = int(input("Enter the ribbon length : "))

    result = classify(length)
    print(result)

    total += length

    if result == "Below range":
        below_range += 1
    elif result == "In range":
        in_range +=1
    else:
        above_range +=1

average = calculate_average(total, count)
print(f"Total length : {total}")
print(f"Average length : {average} cm")
print(f"Below range : {below_range}")
print(f"In range : {in_range}")
print(f"Above range : {above_range}")
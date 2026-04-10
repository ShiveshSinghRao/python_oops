# LIST BASICS

numbers = [10, 20, 30, 40, 50]

# Access
print("First:", numbers[0])
print("Last:", numbers[-1])

# Modify
numbers[2] = 300

# Add
numbers.append(60)

# Remove
numbers.remove(20)

# Loop
for num in numbers:
    print("Number:", num)

# With index
for i in range(len(numbers)):
    print(f"Index {i} -> {numbers[i]}")
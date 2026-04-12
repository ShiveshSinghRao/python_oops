# SET BASICS

nums = {1, 2, 3, 3, 4, 5}

print("Set:", nums)  # duplicates removed

# Add
nums.add(6)

# Remove
nums.remove(2)

# Loop
for n in nums:
    print(n)

# Check existence
if 3 in nums:
    print("3 exists")
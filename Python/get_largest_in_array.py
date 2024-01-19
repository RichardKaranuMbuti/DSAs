nums = [0,1 ,12,24,56,78,33,26]

large = nums[0]

'''
for i in nums:
    if i<large:
        continue
    large = i
print(large)


for i in nums:
    if i>large:
        large = i
print(large)
'''
# Step 1: Split the list into smaller arrays of 2 elements each
small_arrays = [nums[i:i+2] for i in range(0, len(nums), 2)]

# Step 2 & 3: Find the larger number in each pair and append to a new array
larger_numbers = [max(pair) for pair in small_arrays]

# Step 4: Find the largest and second largest numbers
largest = max(larger_numbers)
larger_numbers.remove(largest)
second_largest = max(larger_numbers)

print("Largest number:", largest)
print("Second largest number:", second_largest)


# Approach 2
# Function to find the larger number in a pair
def find_larger(a, b):
    if a > b:
        return a
    else:
        return b

# Step 1 & 2: Iterate and compare elements two at a time
larger_numbers = []
for i in range(0, len(nums), 2):
    if i + 1 < len(nums):
        larger = find_larger(nums[i], nums[i + 1])
        larger_numbers.append(larger)
    else:
        # If the list has an odd number of elements, add the last element as is
        larger_numbers.append(nums[i])

# Step 3: Find the largest and second largest number
largest = None
second_largest = None

for num in larger_numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or num > second_largest:
        second_largest = num

print("Largest number:", largest)
print("Second largest number:", second_largest)
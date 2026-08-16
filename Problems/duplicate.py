# Function to check for duplicates in array
def containsDuplicate(nums):
    # Loop through each element
    for i in range(len(nums)):
        # Compare with all future elements
        for j in range(i + 1, len(nums)):
            # If duplicate found
            if nums[i] == nums[j]:
                return True
    return False

# Sample input
nums = [1, 2, 3, 4, 5, 6, 6, 6,]

# Call function and print result
res = containsDuplicate(nums)
print("true" if res else "false")

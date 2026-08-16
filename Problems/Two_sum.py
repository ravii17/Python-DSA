# A single array is given and we have to find the sum.
Length = int(input("Enter the index length of array: "))
Target = 11
arr = [int(input("Enter the next element of the array here: ")) for i in range(Length)]

print("Array:", arr)

# Find two sum
found = False
for i in range(Length):
    for j in range(i + 1, Length):  # ✓ Fixed: Length (not Lenght)
        if arr[i] + arr[j] == Target:
            print(f"Found: arr[{i}] + arr[{j}] = {arr[i]} + {arr[j]} = {Target}")
            found = True
            break

if not found:
    print("No pair found")
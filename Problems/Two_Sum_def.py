def solve_two_sum(arr, target):
    # Get user input
    n = int(input("Enter array length: "))
    arr = list(map(int, input("Enter elements: ").split()))
    target = int(input("Enter target sum: "))
    
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                print(f"Found: {arr[i]} + {arr[j]} = {target}")
                print(f"Indices: [{i}, {j}]")
                return
    print("No pair found")


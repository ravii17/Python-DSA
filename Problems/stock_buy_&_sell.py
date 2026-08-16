price = int(input("enter price per day"))

a = [int(input("Enter : ")) for i in range (price)]

profit = 0
maxprofit = 0

for i in range (price):
    for j in range (i+1,price):
        profit = a[j]-a[i]
        maxprofit = max(maxprofit, profit)

print("Max Profit is ", maxprofit)
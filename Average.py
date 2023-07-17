import array

a = array.array('i')
print("Enter some numbers to find average.")
n=int(input("First enter how many numbers' average do you want to find."))


# Input numbers and append to array a
for i in range(n):
    x = int(input())
    a.append(x)

# Find the sum of the numbers in array a
sum = 0
for num in a:
    sum += num

# Calculate the average
avg = sum / len(a)

# Print the average
print("The average is:", avg)

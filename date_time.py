import datetime
import time

# Record the starting time
start_time = time.time()

# Your code to measure
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())
print(datetime.datetime.now().day)
print(datetime.datetime.now().month)
print(datetime.datetime.now().time())
now = datetime.datetime.now()
print(now.strftime("%d.%m/%Y     %d %y"))
print(datetime.datetime(2008, 6, 10, 12, 2, 12))

my_date_of_birth = datetime.datetime(2009, 10, 16, 17, 30, 00)
current_time = datetime.datetime.now()

my_exact_age = current_time - my_date_of_birth

print(my_exact_age)

print(4970/365)

# Record the ending time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

# Print the result
print(f"Execution time: {execution_time} seconds")

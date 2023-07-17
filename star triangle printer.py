i = 1
j = 1
k = 1
limit = int(input("Enter a number as limit for Star triangle "))
spacer = limit
while i <= limit:
    k=1
    while k <= spacer:
        print(" ", end="")

        k = k + 1
    spacer = spacer - 1
    j = 1
    while j <= i:
        print("* ", end="")
        j = j + 1
    print()
    i = i + 1



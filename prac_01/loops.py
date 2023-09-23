for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num_stars = int(input("Enter number of stars: "))

print("Number of Stars: ", num_stars)
print('*' * num_stars)

for i in range(num_stars + 1):
    print('*' * i)

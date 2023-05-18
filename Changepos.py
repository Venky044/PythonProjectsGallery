row1 = ["😀", "'😀", "'😀"]
row2 = ["😀", "'😀", "'😀"]
row3 = ["😀", "'😀", "'😀"]

maps = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")
# x, y = int(position[0]), int(position[1])

x, y = map(int, input("Where do you want to put the treasure? "))

maps[x - 1][y - 1] = "x"
print(f"{maps[0]}\n{maps[1]}\n{maps[2]}")

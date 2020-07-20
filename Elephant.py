x = int(input())

steps = 0

steps += x // 5
x = x % 5
steps += x // 4
x = x % 4
steps += x // 4
x = x % 4
steps += x // 3
x = x % 3
steps += x // 2
x = x % 2
steps += x // 1
x = x % 1

print("%d" % (steps))
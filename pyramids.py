# Left-aligned Half Pyramid
print('Pyramid #1: Left-Aligned Half Pyramid')

def pyramid(n):
    for i in range(n):
        for j in range(i):
            print("#", end=" ")
        print()

pyramid(9)
print()

# Right-aligned Half Pyramid (with dots as placeholders)
print('Pyramid #2: Right-Aligned Half Pyramid with dots')

def pyramid(n):
    for i in range(n):
        for j in range(n + i):
            print(".", end=" ")
        for j in range(n - i):
            print("#", end=" ")
        print()
pyramid(9)
print()


# Left-aligned Half Pyramid (with spaces)
print('Pyramid #3: Right-Aligned Half Pyramid with spaces')

def pyramid(n):
    for i in range(n):
        for j in range(n + i):
            print(" ", end=" ")
        for j in range(n - i):
            print("#", end=" ")
        print()
pyramid(9)
print()


# Left aligned full pyramid
print('Pyramid #4: Left-Aligned Full Pyramid')

def pyramid(n):
    for i in range(n):
        for j in range(i):
            print("#", end=" ")
        print()
    for i in range(n, 0, -1):
        for j in range(i):
            print("#", end=" ")
        print()

pyramid(9)
print()



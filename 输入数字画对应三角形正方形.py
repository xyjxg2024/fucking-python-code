def print_square(n):
    for i in range(n):
        for j in range(n):
            print(f"{i * n + j+1:02}", end='')
        print()

def print_triangle(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("  ", end='')
        for j in range(i + 1):
            print(f"{i * (i + 1) // 2 + j+1:02}", end='')
        print()

def main():
    n = int(input().strip())
    print_square(n)
    print()
    print_triangle(n)

main()

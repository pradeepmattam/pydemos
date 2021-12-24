rows = int(input("input the number of rows: "))
columns = int(input("input the number of columns: "))
symbol = input("input the symbol to print: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    columns -= 1
    print()

try:
    with open('test.txt',w) as file:
        file.write("this is great")
except FileNotFoundError as e:
    print(e)
else:
    print(file.close())

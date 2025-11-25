a = str(input())
result = ""
for i in a:
    if i == "-":
        result += "fu "
    elif i == "0":
        result += "ling "
    elif i == "1":
        result += "yi "
    elif i == "2":
        result += "er "
    elif i == "3":
        result += "san "
    elif i == "4":
        result += "si "
    elif i == "5":
        result += "wu "
    elif i == "6":
        result += "liu "
    elif i == "7":
        result += "qi "
    elif i == "8":
        result += "ba "
    else:
        result += "jiu "

result = result.rstrip()
print(result)


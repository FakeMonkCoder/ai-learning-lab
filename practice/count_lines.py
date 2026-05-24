file = open("../notes/today.txt","r")

content = file.read()

lines = content.splitlines()


count = len(lines)


print("This file has",count,"lines")

file.close()
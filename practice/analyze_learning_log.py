
file = open("../notes/today.txt","r")

content = file.read()

lines = content.splitlines()

print("Total lines:",len(lines))

print("Total characters:",len(content))

print("First line:",lines[0])
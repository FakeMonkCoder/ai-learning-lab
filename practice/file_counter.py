import os

content = os.listdir("../notes")

txtcount = 0
jsoncount = 0
mdcount = 0

for co in content:
    if co.endswith(".txt"):
        txtcount += 1
        if co.endswith(".json"):
            jsoncount += 1
        else :
            mdcount += 1

print(".txt",txtcount)
print(".json",jsoncount)
print(".md",mdcount)

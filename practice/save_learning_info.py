import json

learning_info = {
    "name": "Ren",
    "goal": "Enter the AI Field",
    "current_sprint": "Sprint 1",
    "tools": ["Python","Markdown","Git","Github"]
}

file = open("../notes/learning_info.json","w")

json.dump(learning_info,file)

file.close()
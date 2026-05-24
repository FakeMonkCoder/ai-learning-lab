import os


def count_files(folder_path):

    files = os.listdir(folder_path)


    txtcount = 0
    jsoncount = 0
    mdcount = 0

    for co in files:
      if co.endswith(".txt"):
        txtcount += 1
      elif co.endswith(".json"):
            jsoncount += 1
      elif co.endswith(".md"):
            mdcount += 1

    return [txtcount,jsoncount,mdcount]


def print_result(result):

    print(".txt:",result[0])
    print(".json:",result[1])
    print(".md:",result[2])



folder_path = "../notes"

print_result(count_files(folder_path))


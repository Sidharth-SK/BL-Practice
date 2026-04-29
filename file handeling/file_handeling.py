"""
File Handeling:-
1. csv file
2. json file

using: context manager.
Libraries used: csv, json
"""
with open('file handeling\\practice.txt', 'r') as f:
    print(f.read())

    f.seek(0)
    for line in f:
        print(line.strip())
    
    f.seek(0)
    lines = f.readlines()

lines  = ["first line\n", "second line\n", "third line\n"]
with open('file handeling\\practice.txt', 'w') as f:
    f.write("Hello World\n")
    f.writelines(lines)

with open('file handeling\\practice.txt', 'r') as f:
    print(f.read())
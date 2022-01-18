try:
    print(45/0)
except ZeroDivisionError:
    print('Вы не можете делить на 0')

# 2
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Вы не можете делить на 0')
    else:
        print(answer)
"""
# 3

fname = 'analize.txt'
try:
    with open(fname, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry {fname} not found")
else:
    words = content.split()
    k = len(words)
    print(f"The file {fname} has {k} words")

"""
def countwords(fname):
    try:    
        with open(fname, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry {fname} not found")
    else:
        words = content.split()
        k = len(words)
        print(f"The file {fname} has {k} words")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    countwords(filename)
"""


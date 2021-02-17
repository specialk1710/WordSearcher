"""
pass a function in the function def forward
functions for all directions (backward, up, down, up/forward, up/backward, down/forward, down/backward)
"""

a = [["P", "I", "M", "P", "X"],
     ["X", "X", "X", "X", "X"],
     ["X", "X", "X", "X", "X"],
     ["X", "X", "X", "X", "X"],
     ["X", "X", "X", "X", "X"]
    ]
def bounds_right(x, index, length, bounds):
    return x + length - index > bounds

def forward(y, x, word, index):
    if not bounds_right(x, index, len(word), len(a[y])):
        current = a[y][x]
        print(current)
        if current == word[index]: #move into function
            if index + 1 == len(word):
                return True
            return forward(y, x + 1, word, index + 1)
    return False

word = "PIMP"
for y in range(len(a)): #move into function
    for x in range(len(a[y])):
        result = forward(y, x, word, 0)
        if result:
            print("Found word!")
            break
    else:
        continue
    break


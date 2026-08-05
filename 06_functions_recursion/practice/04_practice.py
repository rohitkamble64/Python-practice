# Write a Python function to remove a given word from a list and strip it from the remaining words in the list.

def rem(l, word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

l = ['apple', 'cherry', 'banana', 'Mango']
print(rem(l, "an"))
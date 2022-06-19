alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '’']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
words = """
[words to be editeds]
"""
i=0
while i<len(words):
    if words[i] in alphabet or words[i] in numbers:
        words = words.replace(words[i], '')
    i+=1
print(words)
print(input("").lower())
import re
def convert(word): #Converts letters in a word to their pythagorean indices.
    return [((ord(ch)-ord("A"))%9+1) for ch in word]
def input_parts(): #Returns one number sublist for each input full name part.
    is_name = re.compile("^(?: *[a-zA-Z]+)+ *$")
    full_name = input("Enter your full name: ")
    while not is_name.match(full_name):
        full_name = input("Bad name, try again: ")
    return [convert(p.upper()) for p in full_name.split()]
def combine(numbers): #Reduces a list of numbers to a single number
    while len(numbers)>1:
        numbers = [int(ch) for ch in str(sum(numbers))]
    return numbers[0]
def merge_multiple(parts): #Merges several lists of numbers into a single number
    return combine([combine(p) for p in parts])
def meaning(number): #1<=number<=0. See WJEC spec for meaning of Lucky Number.
    return ["Natural leaders", "Natural peacemakers", "Creative and optimistic",
            "Hard  workers", "Value freedom", "Carers and providers",
            "Thinkers", "Have diplomatic skills", "Selfless and generous"
            ][number-1]
no = merge_multiple(input_parts())
print(no, meaning(no))

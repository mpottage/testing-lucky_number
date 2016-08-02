def convert(word):
    return [((ord(ch)-ord("A"))%9+1) for ch in word]
def input_parts():
    full_name = input("Enter your full name: ")
    return [convert(p.upper()) for p in full_name.split(' ')]
def get_lucky(numbers):
    while len(numbers)>1:
        numbers = [int(ch) for ch in str(sum(numbers))]
    return numbers[0]
def combine(parts):
    return get_lucky([get_lucky(p) for p in parts])
def meaning(number):
    return ["Natural leaders", "Natural peacemakers", "Creative and optimistic",
            "Hard  workers", "Value freedom", "Carers and providers",
            "Thinkers", "Have diplomatic skills", "Selfless and generous"
            ][number-1]
no = combine(input_parts())
print(no, meaning(no))

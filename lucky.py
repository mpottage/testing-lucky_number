def convert(word):
    res = ""
    for ch in word:
        res += str((ord(ch)-ord("A"))%9+1)
    return res
def input_parts():
    full_name = input("Enter your full name: ")
    return [convert(p.upper()) for p in full_name.split(' ')]
def get_lucky(converted_word):
    while len(converted_word)>1:
        converted_word = str(sum([int(ch) for ch in converted_word]))
    return converted_word
def combine(parts):
    res = []
    for p in parts:
        res.append(get_lucky(p))
    return get_lucky(res)
def meaning(number):
    return ["Natural leaders", "Natural peacemakers", "Creative and optimistic",
            "Hard  workers", "Value freedom", "Carers and providers",
            "Thinkers", "Have diplomatic skills", "Selfless and generous"
            ][number-1]
no = int(combine(input_parts()))
print(no, meaning(no))

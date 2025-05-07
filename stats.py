def kembalikan_string(text):
    teks = text.split()
    return len(teks)

def sort_char_and_count(charcountdict):
    sorted_char = []

    for char,count in charcountdict.items():
        sorted_char.append({"char":char, "num":count})

    sorted_char.sort(reverse=True, key=lambda item:item["num"])
    return sorted_char

def count_chars(text):
    char_counts = {}
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

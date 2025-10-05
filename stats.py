def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def count_words(text):
    words = text.split()
    return len(words)

def char_counts(text):
    char = {}
    for c in text.lower():
        if c not in char:
            char[c] = 1
        else:
            char[c] += 1
    return char

def sort_on(item):
    return item['num']

def sort_char_counts(char_count_dict):
    char_list = []
    for char, num in char_count_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key = sort_on)
    return char_list


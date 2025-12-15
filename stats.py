
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def get_num_words(filepath):
    text = get_book_text(filepath)
    return len(text.split())



def get_num_character(filepath):
    text = get_book_text(filepath).lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) +1

    return char_counts

def sort_on(item):
    return item["num"]
    
def get_sorted_characters(char_dict):
    char_list = []

    for char, count in char_dict.items():
        if not char.isalpha():
            continue
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)   
    return char_list
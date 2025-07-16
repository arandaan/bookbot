def count_words(book):
    words = book.split()
    return len(words)

def count_charac(text):
    dict_charac = {}
    for char in text:
        lower = char.lower()
        if lower in dict_charac:
            dict_charac[lower] += 1
        else:
            dict_charac[lower] = 1
    return dict_charac

def sorted(character_counts):
    list_of_dictionaries = []
    for char, count in character_counts.items():
        char_dictionary = {
            "char": char,
            "num": count,
        }
        list_of_dictionaries.append(char_dictionary)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries

def sort_on(items):
    return items["num"]
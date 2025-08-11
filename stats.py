def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    words = text.split()
    repeats = {}
    for word in words:
        for letter in word:
            if letter.lower() in repeats.keys():
                repeats[letter.lower()] += 1
            else:
                repeats[letter.lower()] = 1
    return list_dictionarys(repeats)
                
                
def sort_on(list_dicts):
    return list_dicts["num"]


def list_dictionarys(count_chars):
    dictionarys = []
    for key in count_chars.keys():
        dict = {"char": key, "num": count_chars[key]}
        dictionarys.append(dict)
    dictionarys = sorted(dictionarys, key=sort_on, reverse=True)
    return dictionarys
    
        
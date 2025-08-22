def get_num_words(text):
    words = text.split()
    return len(words)


def number_of_times_character_appears(text):
    lexicon = {}
    for _ in text:
        _ = _.lower() # avoiding duplicates due to case sensitivity
        if _ in lexicon:
            lexicon[_] += 1
        else:
            lexicon[_] = 1
            
    return lexicon
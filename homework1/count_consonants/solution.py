def count_consonants(str):
    return len([character for character in str if
                character.isalpha() and not character in "aeiouyAEIOUY"])

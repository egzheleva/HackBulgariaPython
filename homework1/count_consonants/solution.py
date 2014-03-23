def count_consonants(str):
    consonants = 'bcdfghjklmnpqrstvwxz'
    count = 0
    for i in str:
        if i in consonants:
            count += 1
    return count


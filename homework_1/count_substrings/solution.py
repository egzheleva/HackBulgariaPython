def count_substrings(haystack, needle):
    lst = haystack.split(" ")
    result = 0
    for i in lst:
        if i == needle:
            result += 1
    return result
    
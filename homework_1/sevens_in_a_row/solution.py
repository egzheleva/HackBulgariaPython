import re

def sevens_in_a_row(arr, n):
    return bool(re.search('7' * n, ''.join(map(str, arr))))
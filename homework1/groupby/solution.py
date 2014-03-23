from collections import defaultdict

def groupby(func, seq):
    grouped_items = defaultdict(list)

    for item in seq:
        grouped_items[func(item)].append(item)

    return grouped_items


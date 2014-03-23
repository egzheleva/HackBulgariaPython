from collections import defaultdict


def group_by_type(dictionary):
    grouped_items = defaultdict(dict)
    keys = dictionary.keys()
    for key in keys:
        if not type(key) in grouped_items:
            grouped_items[type(key)] = {key: dictionary[key]}
        else:
            grouped_items[type(key)][key] = dictionary[key]
    return dict(grouped_items)


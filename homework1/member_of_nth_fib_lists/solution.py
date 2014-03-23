def nth_fibonacci_lists(listA, listB, n):
    if n == 1:
        return listA
    if n == 2:
        return listB
    else:
        return nth_fibonacci_lists(listB, listA + listB, n - 1)


def member_of_nth_fib_lists(listA, listB, needle):
    n = 1
    result = []
    while len(result) < len(needle):
        result = nth_fibonacci_lists(listA, listB, n)
        n += 1
    return result == needle


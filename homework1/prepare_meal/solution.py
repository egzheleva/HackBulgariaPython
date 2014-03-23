def count_spam(number):
    spam = 0

    while number % 3 == 0:
        spam += 1
        number /= 3

    return spam


def prepare_meal(number):
    meal = ''

    if number % 3 == 0:
        meal += ' '.join(['spam'] * count_spam(number))

    if number % 5 == 0:
        meal += ' and eggs' if meal else 'eggs'

    return meal.strip()
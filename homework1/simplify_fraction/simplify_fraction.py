def gcd(m, n):
    z = abs(m - n)
    if (m - n) == 0:
        return n
    else:
        return gcd(z, min(m, n))


def simplify_fraction(fraction):
    great = gcd(fraction[0], fraction[1])
    result = (fraction[0] // great, fraction[1] // great)
    return result

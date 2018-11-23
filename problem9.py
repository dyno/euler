def is_tri(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2


def triplet_gen():
    poss = []
    for a in range(501):
        for b in range(501):
            c = 1000 - (a + b)
            if a < b < c and a + b + c == 1000 and is_tri([a, b, c]):
                poss.append([a, b, c])
    return poss


if __name__ == '__main__':
    t = triplet_gen()
    a, b, c = t[0]
    print(a * b * c)

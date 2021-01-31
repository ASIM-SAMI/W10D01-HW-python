import math


def allTriangles(a, b):
    all_triples = math.factorial((a * b) + 3 - 1) / math.factorial(3)
    colinear_triples = 0
    for x1 in range(1, a + 1):
        for y1 in range(1, b + 1):
            for x2 in range(1, a + 1):
                for y2 in range(1, b + 1):
                    for x3 in range(1, a + 1):
                        for y3 in range(1, b + 1):
                            if (y3 - y1) == (y2 - y1 / x2 - x1) * (x3 - x1):
                                colinear_triples += 1
    print("all_triples: ", all_triples)
    print("colinear_triples: ", colinear_triples)

    return all_triples - colinear_triples


allTriangles(21, 7)

import numpy as np


def discrete_distribution(probs):
    cumul = 0
    dist = []

    for val in probs:
        cumul = cumul + val
        dist.append(cumul)

    return dist


def expected_value(vals, probs):
    pairs = zip(vals, probs)
    expected = 0
    for (v, p) in pairs:
        expected = expected + (v * p)

    return expected


def variance(vals, probs):
    expected = expected_value(vals, probs)
    pairs = zip(vals, probs)
    var = 0

    for (v, p) in pairs:
        var = var + ((v - expected) ** 2) * p

    return var

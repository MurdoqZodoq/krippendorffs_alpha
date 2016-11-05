'''Python3 explanatory implementation of Krippendorff's Alpha

For a more thorough (and mathematical) explanation see:
https://github.com/foolswood/krippendorffs_alpha/raw/krippendorff.pdf

This is not intended to be an efficient implementation, but one to help explain
the measure to those for whom python is easier to read than mathematical
notation.
'''

from math import factorial


def D(delta, R, m):
    '''The total disagreement "distance" between all pairs that can be made
    from the multiset m'''
    s = 0.0
    for c in R:
        for k in R:
            s += delta(c, k) * W(m, c, k) / P(len(m), 2)
    return s


def P(n, r):
    '''The number of permutation of length r that can be made from n items'''
    return factorial(n) / factorial(n - r)


def W(m, c, k):
    '''The number of ways that the pair (c, k) can be made from the elements of
    m (without replacement)'''
    if c == k:
        return nu(m, c) * (nu(m, k) - 1)
    else:
        return nu(m, c) * nu(m, k)


def nu(m, e):
    '''Multiplicity'''
    return m.count(e)


def alpha(delta, R, U):
    '''Krippendorff's Alpha'''
    # Eliminate uncomparable result sets
    U = [u for u in U if len(u) > 1]
    # Construct the multiset of all comparable elements
    V = []
    for u in U:
        V += u
    # Disagreement expected by chance
    D_e = D(delta, R, V)
    # Observed disagreement
    D_o = 0
    for u in U:
        D_o += D(delta, R, u) * len(u) / len(V)
    # Alpha
    return 1 - (D_o / D_e)

#!/usr/bin/env python3
'''The "dresses" example from:
https://github.com/foolswood/krippendorffs_alpha/raw/krippendorff.pdf'''

from explanatory import alpha


def nominal_delta(a, b):
    return 0 if a == b else 1

data = {
    ('y', 'n', 'n'),
    ('y', 'n'),
    ('n',)
}

possible_responses = {'y', 'n'}

print(alpha(nominal_delta, possible_responses, data))

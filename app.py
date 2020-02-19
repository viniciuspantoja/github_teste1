from math import pi
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys

def circles(r):
    """renders the area of a circle with a given radius as input

    :param int r: radius
    """

    if r <0:
        raise ValueError("The radius should not be negative.")

    else:
        sys.stdout.write('area = {}'.format(pi * (r **2)))
        return pi * (r **2)


def squares(r):

    if r <= 0:
        raise ValueError('The size of a square should be positive')

    else:
        return r**2

if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="size o radius")

    args = parser.parse_args()
    circles(args.rows)

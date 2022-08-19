from sympy import diag, symbols

from einsteinpy.symbolic import constants
from einsteinpy.symbolic.metric import MetricTensor


def MinkowskiCartesian_2d(c=constants.c):
    """
    Minkowski(flat) space-time in Cartesian coordinates. Space-time without any curvature or matter.

    Parameters
    ----------
    c : ~sympy.core.basic.Basic or int or float
        Any value to assign to speed of light. Defaults to 'c'.


    """
    coords = symbols("t x")
    metric = diag(-1, 1 / (c ** 2)).tolist()
    return MetricTensor(metric, coords, "ll", name="2D_MinkowskiMetric")


Minkowski_2d = MinkowskiCartesian_2d


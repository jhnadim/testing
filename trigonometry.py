import math

class Trigonometry:
    """
    A class for trigonometry operations.

    Supports the following methods:

    - sin(x): compute the sine of x in radians.
    - cos(x): compute the cosine of x in radians.
    - tan(x): compute the tangent of x in radians.
    - sec(x): compute the secant of x in radians.
    - csc(x): compute the cosecant of x in radians.
    """

    def sin(self, x):
        """
        Compute the sine of x in radians.
        """
        return math.sin(x)

    def cos(self, x):
        """
        Compute the cosine of x in radians.
        """
        return math.cos(x)

    def tan(self, x):
        """
        Compute the tangent of x in radians.
        """
        return math.tan(x)

    def sec(self, x):
        """
        Compute the secant of x in radians.
        """
        return 1 / math.cos(x)

    def csc(self, x):
        """
        Compute the cosecant of x in radians.
        """
        return 1 / math.sin(x)

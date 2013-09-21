class CurveData(object):
    def __init__(self, stock_tag):
        """stock_tag is for example "VOLV-B.ST"."""
        pass

    def range(self, from_x, to_x):
        """return ((from_x, y0), (x1, y1), ..., (to_x, yn))"""
        pass

    def range_p(self, from_x, to_x):
        """return derivative ((from_x, y0), (x1, y1), ..., (to_x, yn))"""
        pass

    def value_at_x(self, x):
        """Return y value at x, possibly interpolated?"""
        pass

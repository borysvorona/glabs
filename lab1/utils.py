from sympy import N, symbols, sympify, zoo, diff


class Function(object):
    #   1+ctg(x/2)-(1-2*cos(x/2)**2)+sin(x)**2
    #   1+cot(x/2)-(1-2*cos(x/2)**2)+sin(x)**2
    #   1+(cos(x/2)/sin(x/2))-(1-2*cos(x/2)**2)+sin(x)**2

    def __init__(self, expr, start, end, step):
        self.expr = expr
        self.start = start
        self.end = end
        self.step = step

    @property
    def get_result(self):
        x = symbols('x')
        xx = self.start
        result = []
        while xx <= self.end:
            xx += self.step
            try:
                result.append([float(xx),
                               (None if N(sympify(self.expr).subs(x, xx)) == zoo else N(sympify(self.expr).subs(x, xx)))])
            except Exception as ex:
                print(ex)
        return result

    @property
    def get_ordinate_only(self):
        x = symbols('x')
        xx = self.start
        result = []
        while xx <= self.end:
            xx += self.step
            try:
                result.append(None if N(sympify(self.expr).subs(x, xx)) == zoo else N(sympify(self.expr).subs(x, xx)))
            except Exception as ex:
                print(ex)
        return result

    @property
    def get_abscissa_only(self):
        xx = self.start
        result = []
        while xx <= self.end:
            xx += self.step
            result.append(float(xx))
        return result

    @property
    def count(self):
        xx = self.start
        count = 0
        while xx <= self.end:
            xx += self.step
            count += 1
        return count

    @property
    def middle_point(self):
        return self.start / 2 + self.end / 2


class OrdinaryLeastSquares(object):

    def __init__(self, func):
        self.func = func
        self.n = self.func.count
        self.sum_x = sum(self.func.get_abscissa_only)
        self.sum_y = sum(self.func.get_ordinate_only)
        self.sum_xx = sum([i * i for i in self.func.get_abscissa_only])
        self.sum_xy = sum([i[0]*i[1] for i in self.func.get_result])

    @property
    def get_a(self):
        return (self.n * self.sum_xy - self.sum_x * self.sum_y) / (self.n * self.sum_xx - self.sum_x**2)

    @property
    def get_b(self):
        return (self.sum_y - self.get_a * self.sum_x) / self.n

    @property
    def get_expression(self):
        return '%s * x + %s' % (self.get_a, self.get_b)


class TaylorMethod(object):

    def __init__(self, expr, mpoint):
        self.expr = expr
        self.mpoint = mpoint

    @property
    def get_diff(self):
        return diff(sympify(self.expr))

    @property
    def get_expression(self):
        x = symbols('x')
        answer = N(sympify(self.expr).subs(x, self.mpoint))
        derivative = N(self.get_diff.subs(x, self.mpoint))
        return '%s + %s * (x - %s)' % (answer, derivative, self.mpoint)

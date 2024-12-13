class Interval:
    def __init__(self, lower, upper):
        """
        Конструктор для интервала с границами lower и upper.
        """
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f"[{self.lower}, {self.upper}]"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        """
        Сравнение двух интервалов на равенство.
        """
        return self.lower == other.lower and self.upper == other.upper

    def __hash__(self):
        return hash((self.lower, self.upper))

    def __contains__(self, value):
        """
        Проверка, входит ли значение в интервал.
        """
        return self.lower <= value <= self.upper

    def __len__(self):
        """
        Возвращает длину интервала.
        """
        return self.upper - self.lower

    def __add__(self, other):
        """
        Сложение двух интервалов.
        """
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other):
        """
        Вычитание двух интервалов.
        """
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def __mul__(self, other):
        """
        Умножение двух интервалов.
        """
        results = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(results), max(results))

    def __truediv__(self, other):
        """
        Деление интервалов, проверяя деление на ноль.
        """
        if 0 in other:
            raise ZeroDivisionError("Деление на интервал, содержащий 0")
        return self * Interval(1 / other.lower, 1 / other.upper)

    def __neg__(self):
        """
        Возвращает отрицание интервала.
        """
        return Interval(-self.upper, -self.lower)
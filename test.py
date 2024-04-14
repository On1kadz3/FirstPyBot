import math


def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2


def example_function(x):
    return x ** 3 + x ** 2 - 9*x + 9


root = bisection_method(example_function, -4, -3.8)
print("Корень уравнения x^3 + x^2 - 9*x + 9 =", root)

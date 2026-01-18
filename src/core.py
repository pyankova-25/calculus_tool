import math
import sympy
from typing import Union, Tuple, Optional


class CalculusTool:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Ошибка: Деление на ноль невозможно.")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return math.pow(a, b)

    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> Union[Tuple[float, float], Tuple[float], None]:
        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен 0 для квадратного уравнения.")

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return (x1, x2)
        elif discriminant == 0:
            x = -b / (2 * a)
            return (x,)
        else:
            return None

    @staticmethod
    def get_derivative(expression: str, variable: str = 'x') -> str:
        try:
            x = sympy.symbols(variable)
            expr = sympy.sympify(expression)
            derivative = sympy.diff(expr, x)
            return str(derivative)
        except Exception as e:
            raise ValueError(f"Некорректное выражение: {e}")

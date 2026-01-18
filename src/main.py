import sys
from core import CalculusTool


def print_menu():
    print("\n--- Calculus Tool v1.1 ---")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Решить квадратное уравнение (ax^2 + bx + c = 0)")
    print("7. Найти производную функции (d/dx)")
    print("0. Выход")


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")


def main():
    calc = CalculusTool()

    while True:
        print_menu()
        choice = input("Выберите операцию: ").strip()

        if choice == '0':
            print("Выход из программы.")
            sys.exit(0)

        try:
            if choice in ['1', '2', '3', '4', '5']:
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")

                if choice == '1':
                    print(f"Результат: {calc.add(a, b)}")
                elif choice == '2':
                    print(f"Результат: {calc.subtract(a, b)}")
                elif choice == '3':
                    print(f"Результат: {calc.multiply(a, b)}")
                elif choice == '4':
                    print(f"Результат: {calc.divide(a, b)}")
                elif choice == '5':
                    print(f"Результат: {calc.power(a, b)}")

            elif choice == '6':
                print("Решение ax^2 + bx + c = 0")
                a = get_number("Введите a: ")
                b = get_number("Введите b: ")
                c = get_number("Введите c: ")
                roots = calc.solve_quadratic(a, b, c)
                if roots is None:
                    print("Корней нет.")
                else:
                    print(f"Корни: {roots}")

            elif choice == '7':
                print("Введите функцию от x (например: x**2 + 3*x + sin(x))")
                expr = input("f(x) = ")
                res = calc.get_derivative(expr)
                print(f"f'(x) = {res}")

            else:
                print("Неверный выбор.")

        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

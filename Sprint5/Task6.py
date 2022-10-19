import cmath

def solve_quadric_equation(a, b, c):
    try:
        d = (int(b) ** 2) - (4 * int(a) * int(c))
        x1 = (-int(b) - cmath.sqrt(int(d))) / (2 * int(a))
        x2 = (-int(b) + cmath.sqrt(int(d))) / (2 * int(a))
        return f'The solution are x1={x1} and x2={x2}'
    except ValueError:
        return 'Could not convert string to float'
    except ZeroDivisionError:
        return 'Zero Division Error'


if __name__ == '__main__':
    print(solve_quadric_equation(1, 5, 6))  # output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"
    print(solve_quadric_equation(0, 8, 1))  # output:   "Zero Division Error"
    print(solve_quadric_equation(1,'abc', 5))  # output:   "Could not convert string to float"
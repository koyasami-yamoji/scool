import random


def generate_equation():

    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)

    first_action = '-' if random.randint(0, 1) == 0 else '+'

    if first_action == '-':
        b = -abs(b)
        first_action = ''
        second_action = '+'
    else:
        second_action = '-' if random.randint(0, 1) == 0 else '+'
        if second_action == '-':
            c = -abs(b)
            second_action = ''

    equation = f'{a}x^2{first_action}{b}x{second_action}{c}=0'

    disc = b**2 - 4 * a * c
    if disc < 0:
        return equation, 'нет решения'
    elif disc == 0:
        x = round(-b / (2 * a), 2)
        return equation, str(x)
    else:
        x1 = round((-b + disc ** 0.5) / (2 * a), 2)
        x2 = round((-b - disc ** 0.5) / (2 * a), 2)
        answer = f'{x1};{x2}'
        return equation, answer

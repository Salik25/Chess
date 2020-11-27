def chek_color(x, y, x2, y2): # функция для проверки цвета двух полей
    if (x + y + x2 + y2) % 2 == 0:
        answer = 'Поля одинакового цвета'
        return answer
    else:
        answer = 'Поля разного цвета'
        return answer


def chek_queen(x, y, x2, y2): # бьет ли поле ферзь
    if x == x2 or y == y2:
        answer = 'Ферзь бьет'
        return answer
    elif x + y == x2 + y2 or x - y == x2 - y2:
        answer = 'Ферзь бьет'
        return answer
    else:
        answer = 'Ферзь не бьет'
        return answer


def chek_horse(x, y, x2, y2): # бьет ли поле конь
    if (abs(x - x2) == 1) and (abs(y - y2) == 2):
        answer = 'Конь бьет'
        return answer
    else:
        answer = 'Конь не бьет'
        return answer


def rook_walk(x, y, x2, y2): # как ходит ладья
    if x == x2 or y == y2:
        answer = 'Можно дойти за 1 ход ладьей'
        return answer
    if y + y2 == x + x2:
        answer = f'Можно дойти за два хода. Промежуточный поле будет {x}:{y2}'
        return answer


def queen_walk(x, y, x2, y2): # как ходит ферзь
    if (x == x2 or y == y2) or (x + y == x2 + y2 or x - y == x2 - y2):
        answer = 'Можно дойти за 1 ход ферзем'
        return answer
    else:
        answer = f'Можно дойти за два хода. Промежуточный поле будет {x}:{y2}'
        return answer


def elephant_walk(x, y, x2, y2): # как ходит слон
    if abs(x - x2) == abs(y - y2):
        answer = 'Можно дойти за 1 ход слоном'
        return answer
    elif abs(x - x2) % 2 == abs(y - y2) % 2:
        for i in range(1, 9):
            for j in range(1, 9):
                if abs(i - x) == abs(j - y) and abs(i - x2) == abs(j - y2):
                    answer = f'Можно дойти за два хода. Промежуточный поле будет {i}:{j}'
                    return answer
    else:
        answer = 'Нельзя дойти слоном'
        return answer


if __name__ == '__main__':
    k = int(input('Введите номер 1 поля от 1-8: '))
    I = int(input('Введите номер 2 поля от 1-8: '))
    m = int(input('Введите номер 3 поля от 1-8: '))
    n = int(input('Введите номер 4 поля от 1-8: '))
    print(chek_color(k, I, m, n))
    print(chek_queen(k, I, m, n))
    print(chek_horse(k, I, m, n))
    print(rook_walk(k, I, m, n))
    print(queen_walk(k, I, m, n))
    print(elephant_walk(k, I, m, n))

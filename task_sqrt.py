def discriminant(a, b, c):
    return b ** 2 - 4 * a * c 


def solution(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        print((-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a))
    elif d == 0:
        print(-b/(2 * a))
    else:
        print('корней нет')

if __name__ == '__main__':
    solution(1, 8, 15) 
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
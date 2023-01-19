def debug(func):
    def wrapper(*args, **kwargs):
        print(f'вызвана функция {func.__name__} с позиционными аргументами - {args} и ключевыми аргументами - {kwargs}')
        call = func(*args, **kwargs)
        print(f'функция возвращает значение - {call}')
        return call

    return wrapper


@debug
def example(*args, **kwargs):
    even = []
    odd = []
    for i in args:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for j in kwargs.values():
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    print(even)
    print(odd)
    return f'список четных чисел - {even}, список нечетных чисел - {odd}'


example(15, 456, 1, 9, 12, a=67, k=54, c=8)

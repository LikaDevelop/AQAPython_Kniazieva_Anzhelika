def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        b = 1
        return a / b + 1
    except Exception as unknown_exception:
        print(unknown_exception)


#assert (divide(10, 0)) == 5


class ExceptionClass:
    def some_func(self):
        #raise NotImplementedError
        pass


#ExceptionClass.some_func()

#print(5+'5')

def calculate_anything(a: int):
    """
    This function can accept only integer from 1 to 5
    :return:
    """

    if a in range(0, 5):
        print(a)
    else:
        raise ValueError('You should use only integer from 0 to 5')

#calculate_anything(6)

try:
    1/0
except ZeroDivisionError as error:
    print(error)
else:
    pass
finally:
    pass


class MyOwnException(Exception):
    pass

def my_func_with_exeption(a: int):
    if not type(a) is int:
        raise MyOwnException(f'має бути число, а не те що ти сюди передав: {type(a)}')

try:
    my_func_with_exeption('5')
except MyOwnException as e:
    print(e)


class ValueSholdBeFromOneToFiveException(Exception):
    pass

def func_(a: int):
    if a not in range(0, 5+1):
        raise ValueSholdBeFromOneToFiveException

try:
    func_(5)
except ValueSholdBeFromOneToFiveException as e:
    print(e)
else:
    print('No exception is rize')
finally:
    print('А я тут як тут завжди щось виконую')




tup = (1, 2, 3)
try:
    list(tup)[0] = 5
except TypeError:
    print('Все добре, помилка виникла')
else:
    print('Погано, не виникло помилки')
finally:
    print('А я взагалі завжди виконуюсь')
# 1.   Створити функцію, що приймає число з консолі (використати фунцію input());
#   Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int() спробувати конвертувати рядок в число (input() завжди повертає рядок).
#   Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data".


def func_input_from_console():
    num = int(input())
    return num


try:
    func_input_from_console()
except:
    print("Entered not valid data")


# 2.  Створити функцію, що приймає 2 рядки;
#   Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки), якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.

def two_str(str1: str, str2: str):
    try:
        num1 = int(str1)
        num2 = int(str2)
    except ValueError:
        print(str1 + str2)
    else:
        print(num1 + num2)


two_str('3', '3')


# 3.  Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
#   тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
# Коли користувач вводить число, дякуємо йому )

def input_int_from_console():
    isnotint = True
    while isnotint:
        a: str = input()
        try:
            anum = int(a)
        except:
            print('Input any another symbol')
        else:
            isnotint = False
            print("Thank for working!")

input_int_from_console()

#
# 4.   Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
#   Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його (return)

class OnlyEvenError(Exception):
    pass
def check_digit(a: int):
    if a % 2 == 1:
        raise OnlyEvenError
    else:
        return a


try:
    check_digit(2)
except OnlyEvenError:
    print('OnlyEvenError is work!')
else:
    print('Це число парне!')

#
# 5.  Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit, в яку передавати це число.
#   Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1. Інакше, помножити число на 2.
#   Результат виводити в консоль.
#   Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую".
# Використовувати try-except-else-finally

def new_function(a: int):
    try:
        check_digit(a)
    except:
        print('Помилка')
        print(a + 1)
    else:
        print('Все добре!')
        print( a * 2)
    finally:
        print("Я все одно завжди щось друкую")


new_function(2)

def print_digit(digit: int or float or str):
    if type(digit) not in (int, float, str):
        raise TypeError(f'{digit} is not in int, float, str; given {type(digit)}')
    if type(digit) in (int, float):
        print(digit)
    elif type(digit) is str:
        try:
            if '.' in digit:
                try:
                    print(float(digit))
                except Exception:
                    raise
            else:
                print(int(digit))
        except Exception:
            print(f'Incorrect digit: {digit}, should be in (int, float, stringified int or float)')
    else:
        raise TypeError(f'Incorrect digit: {digit}, should be in (int, float, stringified int or float)')

print_digit(345)
print_digit(345.55)
print_digit('12')
print_digit('12.5678')
print_digit([1]) #Має бути помилка!
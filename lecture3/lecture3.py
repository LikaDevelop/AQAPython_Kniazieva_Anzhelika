counter = 0

while True:
    print("Hello")
    counter += 1
    if counter == 10000:
        break



for lit in 'My favourite text':
    print(lit)

def make_interesting(any_str: str) -> str:
    '''
    :param any_str: any string you want to print with stars
    :return: updated string
    '''
    data = ''
    for sym in any_str:
        data += sym +'*'
    return data

print(make_interesting('Hello, world!'))

class MyClass:
    pass


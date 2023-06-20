riadok = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'

#Розбити рядок на список окремих слів

word_list = riadok.split(' ')
print(word_list)

#Замінити в кожному слові усі голосні літери іншим символом, наприклад #

new_riadok = ''
golosni_list = [ 'й', 'у', 'е', 'ї', 'і', 'а', 'о', 'є', 'я', 'и', 'ю']

for l in riadok:
    if l in golosni_list:
        new_riadok += '#'
    else:
        new_riadok += l

print(new_riadok)

#розбір домашки

vowels = 'йуеїіаоєяию'

def replace_vowels(word):
    new = ''
    for char in vowels:
        new = word.replace(char, '#')
        word = new
    return new

print(' '.join([replace_vowels(word) for word in word_list]))


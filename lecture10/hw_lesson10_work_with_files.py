
# Читання файлу:
#         Відкрийте файл з текстовим вмістом.
#         Прочитайте весь вміст файлу.
#         Виведіть зчитаний вміст на екран.

with open('file_for_reading.txt', 'r') as file:
    print(file.read())

#     Запис у файл:
#         Створіть новий файл або відкрийте існуючий.
#         Запишіть у файл деякий текст.
#         Закрийте файл.

file = open('file_for_writing.txt', 'w')
file.write('Some text')
file.close()

#     Пошук і заміна:
#         Відкрийте файл з текстом.
#         Прочитайте весь вміст файлу.
#         Знайдіть певне слово або фразу у тексті.
#         Замініть знайдену фразу на іншу.
#         Запишіть змінений текст назад у файл.

with open('file_for_changing.txt', 'r+') as file:
    text = file.read()
    text_every_word = text.split(' ')
    if 'Hello' in text_every_word:
        text_every_word[text_every_word.index('Hello')] = 'Goodbye'
    file.seek(0)
    file.truncate()
    file.write(' '.join(text_every_word))


#     Лічильник слів:
#         Відкрийте файл з текстом.
#         Прочитайте весь вміст файлу.
#         Порахуйте кількість слів у тексті.
#         Виведіть результат на екран.

with open('file_with_text.txt', 'r') as file:
    text = file.read()
    words = text.split(' ')
    print(len(words))

#     Аналіз лог-файлу:
#         Відкрийте лог-файл.
#         Прочитайте весь вміст файлу.
#         Знайдіть певні події або помилки у логах.
#         Виведіть знайдені події на екран або запишіть їх у новий файл.

with open('qalight.log', 'r') as logfile:
    info_list = ''
    error_list = ''

    all_log = logfile.readlines()
    for line in all_log:
        if 'INFO' in line:
            info_list += line
        if 'ERROR' in line:
            error_list += line

print(error_list)


#     Копіювання файлу:
#         Відкрийте вихідний файл, який потрібно скопіювати.
#         Відкрийте цільовий файл, куди буде здійснюватися копіювання.
#         Прочитайте вміст вихідного файлу.
#         Запишіть зчитаний вміст у цільовий файл.
#         Закрийте обидва файли.


with open('file_which_copy.txt', 'r') as file:
    text = file.read()

with open('file_for_copy.txt', 'w') as copyfile:
    copyfile.write(text)

file.close()
copyfile.close()
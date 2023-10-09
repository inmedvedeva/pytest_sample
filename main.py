"""

text - это предложение без знаков препинания, слова в котором разделены пробелами.
        Функция должна вернуть 'PASS', если ни одно из слов не находится в черном списке
        и хотя бы одно слово находится в белом списке, иначе - 'FAIL'

Предлагается:
    - написать функцию, реализующую эту логику,
    - написать тесты, покрывающие данную функциональность с использованием модуля pytest.

Например,
    черный список: 'and', 'or', 'not'
    белый список: 'name', 'tag'

"""

white_list = ['name', 'tag']
black_list =['and', 'or', 'not']


def check_list(text):
    for i in text.split():
        if i in white_list and i not in black_list:
            return 'PASS'
        elif i in black_list:
            return 'FAIL'


text_pass = 'Hello it is test name'
text_fail = 'Hello or it is test name'

print(check_list(text_pass))
print(check_list(text_fail))

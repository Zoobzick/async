import subprocess
import locale

""" 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
    проверить тип и содержание соответствующих переменных. Затем с помощью
    онлайн-конвертера преобразовать строковые представление в формат Unicode и также
    проверить тип и содержимое переменных."""

development = "разработка"
socket = "сокет"
decorator = "декоратор"
print(development, type(development))
print(socket, type(socket))
print(decorator, type(decorator))
print("************" * 10, '\n')

development_unicode = "\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430"
socket_unicode = "\u0441\u043E\u043A\u0435\u0442"
decorator_unicode = "\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440"
print(development_unicode, type(development_unicode))
print(socket_unicode, type(socket_unicode))
print(decorator_unicode, type(decorator_unicode))
print("************" * 10, '\n')

""" Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
    последовательность кодов (не используя методы encode и decode) и определить тип,
    содержимое и длину соответствующих переменных."""

cls = b"class"
fnc = b"function"
meth = b"method"
print(cls, type(cls), len(cls))
print(fnc, type(fnc), len(fnc))
print(meth, type(meth), len(meth))
print("************" * 10, '\n')

""" 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
    байтовом типе."""

f_word = b'attribute'
# s_word = b"класс"
# th_word = b"функция"
fth_word = b"type"

# 'класс' и 'функция', байтовый тип данных может содержать только символы из таблицы ASCII


""" 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
    строкового представления в байтовое и выполнить обратное преобразование (используя
    методы encode и decode)."""

words = ['разработка', 'администрирование', 'protocol', 'standard']
for el in words:
    el_encoded = el.encode('utf-8')
    print(el_encoded, el_encoded.decode('utf-8'))
print("************" * 10, '\n')

""" 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
    байтовового в строковый тип на кириллице."""

args = ['ping', 'yandex.ru']

subprocess_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subprocess_ping.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))
print("************" * 10, '\n')

""" 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
    программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
    Принудительно открыть файл в формате Unicode и вывести его содержимое."""

def_encoding = locale.getpreferredencoding()
print(def_encoding)

with open('test_file.txt', 'r', encoding='utf-8') as f:
    print(f)
    for el in f:
        print(el)

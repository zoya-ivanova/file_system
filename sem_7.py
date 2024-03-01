# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

__all__ = ['fill_file_num', 'fill_file_name', 'fill_num_names_file', 'create_file_with_ext', 'gen_files', ]

import random as rnd

_MIN_VALUE: int = -1000
_MAX_VALUE: int = 1000
_DELIMITER: str = "|"

_VOWELS = "AEIOUY"
_CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
_MIN_LEN = 4
_MAX_LEN = 7

def fill_file_num(file_name: str, str_count: int):
    """Заполнение файла случайными числами

    :file_name: Имя файла для сохранения.
    :str_count: Кол-во генерируемых пар значений.
    """
    with open(file_name, "a", encoding="UTF-8") as f:
        for _ in range(str_count):
            number_1 = rnd.randint(_MIN_VALUE, _MAX_VALUE)
            number_2 = rnd.uniform(_MIN_VALUE, _MAX_VALUE)
            f.write(f"{number_1}{_DELIMITER}{number_2}\n")


# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

def fill_file_name(file_name: str, name_count: int):
    """Заполнение файла случайными именами

    :file_name: Имя файла для сохранения.
    :name_count: Кол-во генерируемых имен.
    """
    names = []
    for _ in range(name_count):
        len_name = rnd.randint(_MIN_LEN, _MAX_LEN)
        name = ""
        for i in range(len_name):
            if i % 3 != 0:
                name += _get_char(_CONSONANTS)
            else:
                name += _get_char(_VOWELS)
        names.append(name)
    with open(file_name, "w", encoding="UTF-8") as f:
        f.writelines('\n'.join(names))


def _get_char(string: str) -> str:
    """Получить символ"""
    pos = rnd.randint(0, len(string) - 1)
    return string[pos]


# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

def fill_num_names_file(num_file: str, name_file: str, destination: str):
    """Генерация нового файла их файлов имен и цифр

    :num_file: Файл с цифрами.
    :name_file: Файл с именами.
    :destination: Результирующий файл.
    """
    with (
        open(num_file, "r", encoding="UTF-8") as f_num,
        open(name_file, "r", encoding="UTF-8") as f_name,
    ):
        list_num = [int(n[0]) * float(n[1]) for n in map(lambda x: x.split(_DELIMITER), list(f_num))]
        list_names = [s.replace("\n", '') for s in list(f_name)]
    # формирование нового списка значений
    count_names = len(list_names)
    count_nums = len(list_num)
    count_new_item = max(count_nums, count_names)
    num_pos = name_pos = 0
    new_list = []
    for _ in range(count_new_item):
        if list_num[num_pos] < 0:
            new_list.append(f"{list_names[name_pos].lower()} - {abs(list_num[num_pos])}")
        else:
            new_list.append(f"{list_names[name_pos]} - {round(list_num[num_pos])}")
        num_pos += 1
        name_pos += 1
        if num_pos == count_nums:
            num_pos = 0
        if name_pos == count_names:
            name_pos = 0
    # Запись нового списка в файл
    with open(destination, "w", encoding="UTF-8") as f_new:
        f_new.writelines('\n'.join(new_list))


# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

def create_file_with_ext(extension: str, /, min_len: int = 6, max_len: int = 30, min_rand_bytes: int = 256,
                         max_rand_bytes: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        file_name = set()
        for _ in range(rnd.randint(min_len, max_len)):
            file_name.add(chr(rnd.randint(ord('a'), ord('z'))))

        full_name = ''.join(file_name) + "." + extension
        with open(full_name, "bw") as file:
            file.write(bytes(rnd.randint(0, 255) for _ in range(rnd.randint(min_rand_bytes, max_rand_bytes))))


# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

def gen_files(extensions: list[str]):
    for e in extensions:
        create_file_with_ext(e, count_files=1)


if __name__ == "__main__":
    fill_file_num("numeric.txt", 10)
    fill_file_name("names.txt", 10)
    fill_num_names_file("numeric.txt", "names.txt", "new.txt")
    create_file_with_ext("txt", count_files=5)
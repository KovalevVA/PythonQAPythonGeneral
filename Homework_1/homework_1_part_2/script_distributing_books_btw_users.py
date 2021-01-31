import json, csv

def read_books_file():

    '''Данная функция читает файл books.csv, составвляет словарь, ключи которого представляют собой строки заголовков
    колонок csv файла: 'Title', 'Author' и 'Height', а значения соответсвуют данным, записанным в эти колонки
    на пересечении с каждой строкой, прочитанной на каждой итерации. При вызове функция возвращает объект генератор,
    который содержит словарь с необходимым для дальнейшей работы набором данных'''

    with open('../data_files/books.csv', 'r') as books_csv:
        csv_reader = csv.DictReader(books_csv)
        books_dict = {}
        for row in csv_reader:
            books_dict['Title'] = row['Title']
            books_dict['Author'] = row['Author']
            books_dict['Height'] = row['Height']
            yield books_dict


def read_users_file():

    '''Данная функция очищает результирующий файл example.json во время каждого вызова. Далее читает файл users.json и
    формирует словарь с необходимым набором данных для пользователя. Далее для каждого пользователя
    вызывает генератор функции read_books_file, чтобы получить словарь с книгой, которую получит пользователь.
    Соответственно, если пользователей больше, чем книг либо количество пользователей равно количеству книг, то каждый
    пользователь получит по книге, а в случае, если книг меньше, то для каждого избыточного пользоваеля сработает перехват
    исключения StopIteration и пользователю будет передан пустой список в качестве значения элемента books.
    '''

    with open('../data_files/example.json', 'w') as f:
        f.truncate(0)

    with open('../data_files/users.json', 'r') as text_file:
        text_str = text_file.read()

    dictionary_from_json = json.loads(text_str)
    books_gen = read_books_file()

    for id in dictionary_from_json:

        user = {
            'name' : id['name'], 'gender' :  id['gender'], 'address' : id['address']
        }

        try:

            books = books_gen.__next__()
            write_result_file(user, books)

        except StopIteration:
            books = []
            write_result_file(user, books)

def write_result_file(user, books):

    '''Данная функция записывает результирующий по каждому пользователю словарь в файл
    example.json. Принимает на вход две переменных users и books. В случае, если в качестве books передан пустой список, то
    и в элемент books результирующего словаря для пользователя из словаря user запишется пустой список. В случае, если
    в качестве books передан словарь, то данный словрь будет записан в качестве значения элемента books '''

    user['books'] = []

    if isinstance(books, dict):
        user['books'].append(books)

    cool_json = json.dumps(user, indent=4)
    with open('../data_files/example.json', 'a') as example_file:
        example_file.write(cool_json + '\n\n')

# if __name__ == '__main__':
read_users_file()
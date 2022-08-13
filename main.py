import uuid
import os
from os import walk
import shutil

class Book:
    def __init__(self, name_book):
        self.name_book = name_book
        self.book_id = uuid.uuid4()
        self.chapters = 0
        tree = os.walk(name_book)
        for root, dirs, files in tree:
            for file in files:
                self.chapters += 1
        self.chapters -= 1
        try:
            os.mkdir(name_book)
        except FileExistsError:
            pass

        file = open(os.path.join(name_book, 'info.txt'), 'w', encoding='utf-8')
        file.write('Книга: ' + self.name_book + '\n')
        file.write('Персональный ID = ' + str(self.book_id) + '\n')
        file.write('Количество глав = ' + str(self.chapters) + '\n')
        file.close()

    def new_chapter(self, name_book, name_chapter):  # новая глава
        file = open(os.path.join(name_book, str(name_chapter+'.txt')), 'w', encoding='utf-8')
        file.close()

    def edit_chapter(self, name_book, name_chapter):  # изменить главу
        file = open(os.path.join(name_book, str(name_chapter)+'.txt'), 'a', encoding='utf-8')
        edit = str(input('Введите, что нужно добавить \n'))
        file.write(edit)
        file.close()

    def delete_chapter(self, name_book, name_chapter):  # удалить главу
        try:
            os.remove(name_book + "/" + name_chapter + '.txt')
        except FileNotFoundError:
            print('Такого файла нет')

    def delete_book(self, name_book):  # удалить книгу
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name_book)
        shutil.rmtree(path)

    def update_info(self, name_book):  # обновить info.txt
        self.chapters = 0
        tree = os.walk(name_book)
        for root, dirs, files in tree:
            for file in files:
                self.chapters += 1
        self.chapters -= 1
        file = open(os.path.join(name_book, 'info.txt'), 'w', encoding='utf-8')
        file.write('Книга: ' + self.name_book + '\n')
        file.write('Персональный ID = ' + str(self.book_id) + '\n')
        file.write('Количество глав = ' + str(self.chapters) + '\n')
        file.close()

    @staticmethod
    def list_book():  # список всех книг и кол-во глав к ним
        chapters = -1
        for root, dirs, files in os.walk("."):
            root = str(root[2::])
            if root != '':
                print('\nКнига: ' + root)
            else:
                continue
            chapters = -1
            for filename in files:
                chapters += 1
            print('Количество глав = ' + str(chapters))

    @staticmethod
    def check_book(name_book):  # проверить существует ли книга
        for root, dirs, files in os.walk('.'):
            if str(name_book) == str(root[2::]):
                return True
            else:
                continue

loop = True
print('Добро пожаловать в редактор библиотеки')
while loop is True:
    choice = int(input('\nЧто вы хотите сделать?\n Добавить книгу - 1, добавить главу к книге - 2, дописать главу - 3, удаление главы - 4, удаление книги - 5, вывод всех книг - 6, выйти - 0\n'))
    if choice == 1:
        name_book = str(input('Введите название книги\n'))
        name_book = Book(name_book)
        print('Успешно')

    elif choice == 2:
        name_book = str(input('К какой книге вы хотите добавить главу? \n'))
        if Book.check_book(name_book) is True:
            chapter = str(input('Введите название главы \n'))
            book_any = Book(name_book)
            book_any.new_chapter(name_book, chapter)
            print('Успешно')
        else:
            print('Такой книги нет')

    elif choice == 3:
        name_book = str(input('Главу какой книги вы хотите дописать?\n'))
        if Book.check_book(name_book) is True:
            chapter = str(input('Название главы\n'))
            book_any = Book(name_book)
            book_any.edit_chapter(name_book, chapter)
            print('Успешно')
        else:
            print('Такой книги нет')

    elif choice == 4:
        name_book = str(input('Главу какой книги вы хотите удалить?\n'))
        if Book.check_book(name_book) is True:
            chapter = str(input('Введите название главы \n'))
            book_any = Book(name_book)
            book_any.delete_chapter(name_book, chapter)
            print('Успешно')
        else:
            print('Такой книги нет')

    elif choice == 5:
        name_book = str(input('Введите название книги, которую вы хотите удалить\n'))
        if Book.check_book(name_book) is True:
            book_any = Book(name_book)
            book_any.delete_book(name_book)
            print('Успешно')
        else:
            print('Такой книги нет')

    elif choice == 6:
        Book.list_book()

    elif choice == 0:
        loop = False
        print('Всего доброго!')

    else:
        print('Ошибка')

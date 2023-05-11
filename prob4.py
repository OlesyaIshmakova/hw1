import csv, json
from file import CSV_F_PATH, JSON_F_PATH

# печатает все строки из файла работало
with open(CSV_F_PATH) as csv_file:
    rd = csv.DictReader(csv_file)
    # обнулитьсписок
books = []
for row in rd:
    books.append(row)
print(book)
# list.append(item)     append()      принимает      один      аргумент      item      и      добавляет     его      в      конец      list.

# открыть json пользователи прочитать 
with open(JSON_F_PATH) as json_file:
    users = json.load(json_file)
    users_list = users['users']
    # print(users_list)
num_users = len(users_list)
num_books = len(books)
print(num_users)
print(num_books)

data = [
    {
        "name": "Lolita Lynn",
        "gender": "female",
        "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
        "age": 34,
        "books": [
            {
                "title": "Fundamentals of Wavelets",
                "author": "Goswami, Jaideva",
                "pages": 228,
                "genre": "signal_processing"
            }
        ]
    }
]

max_books_per_user = num_books // num_users
remaining_books = num_books % num_users
print(max_books_per_user)
print(remaining_books)

book_index = 0
for i, user in enumerate(users_list):
    for j in range(max_books_per_user):
        user["books"].append(books[book_index])
        book_index += 1
    if i < remaining_books:
        user['books'].append(books[book_index])
        book_index += 1

with open('result.json', 'w') as f:
    s = json.dumps(data, f)
    f.write(s)

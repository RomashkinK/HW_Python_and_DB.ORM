import json
import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables, Publisher, Book, Stock, Shop, Sale

DSN = "postgresql://postgres:postgres@localhost:5432/hw_ORM_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# with open('book_data.json', 'r') as bd:
#     data = json.load(bd)

# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()
# session.close()

if __name__ == '__main__':

# принимает имя или идентификатор издателя (publisher), например, через input(). Выводит построчно факты покупки книг у этого издателя:
# название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки
# Пример (было введено имя автора — Пушкин):

# Капитанская дочка | Буквоед     | 600 | 09-11-2022
# Руслан и Людмила  | Буквоед     | 500 | 08-11-2022
# Капитанская дочка | Лабиринт    | 580 | 05-11-2022
# Евгений Онегин    | Книжный дом | 490 | 02-11-2022
# Капитанская дочка | Буквоед     | 600 | 26-10-2022

    q = input('Введите имя или идентификатор издателя: ')
    if q.isdigit():
        books = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
        .join(Publisher).join(Stock).join(Sale).join(Shop)\
        .filter(Publisher.id == q)
        #.filter(Publisher.id == q).order_by(Sale.date_sale)
        
            
    else:
        books = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
        .join(Publisher).join(Stock).join(Sale).join(Shop)\
        .filter(Publisher.name.like(f'%{q}%'))
        #.filter(Publisher.name == q).order_by(Sale.date_sale)

    print('Название книги | Название магазина, в котором была куплена эта книга | Стоимость покупки | Дата покупки')

    for book in books:
        print(f'{book.title} | {book.name} | {book.price} | {book.date_sale}')


        

    

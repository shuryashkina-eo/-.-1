# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strings = 50
symbols = 25
weight = 4
final_weight = pages * strings * symbols * weight / ( 1024 ** 2 )
amount_of_books = 1.44 / final_weight
amount_of_books = round (amount_of_books)
print("Количество книг, помещающихся на дискету:", amount_of_books )

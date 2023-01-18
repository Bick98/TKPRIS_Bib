import pandas as pd


def get_books(con):
    return pd.read_sql('''

     WITH get_authors(ID_Book, authors_name)
         AS (SELECT ID_Book, GROUP_CONCAT(name)
             FROM author
                      JOIN book_author USING (ID_Author)
             GROUP BY ID_Book),
        get_tag(ID_Book, tag_book)
         AS (SELECT ID_Book, tag
             FROM book_tag
                      JOIN tag USING (ID_Tag)
             GROUP BY ID_Book)

    SELECT ID_Book AS 'Номер',
    authors_name AS 'Авторы',
    nameBook AS 'Название',
    part AS 'Том',
    year AS 'Год Издания',
    tag_book AS 'Тэг',
    type AS 'Тип'
    FROM book
        LEFT JOIN type USING (ID_Type)
        LEFT JOIN get_authors USING (ID_Book)
        LEFT JOIN get_tag USING (ID_Book)
        LEFT JOIN copy USING (ID_Book)
    ORDER BY ID_Book 
    ''', con)
import psycopg2 as pc #импортируем драйвер для работы
 
conn = pc.connect(  # начинаем конект к бд
    host='YOUR_HOST', # устанавливаем хост
    user='YOUR_USERNAME',  # устанавливаем юзернейм
    dbname='YOUR_DATABASE', # устанавливаем название бдшки
    password='YOUR_PASSWORD' # устанавливаем пароль
)

cur = conn.cursor() #делаем курсор он необходим для дальнейшей работы с запросами

"""типы данных(распрастраненные): VARCHAR() - позволяет писать елементы но с ограничением на текст, INT - числа как в пайтоне, TEXT - неограниченное количевство символов, PRIMARY KEY - главный ключ, NULL - означает что строка может быть пустой, NOT NULL - означает что строка не может быть пустой"""
"""execute используем для SQL-ЗАПРОСА, CREATE TABLE - создаем таблицу , IF NOT EXISTS TABLE_NAME - приставка которая проверяем есть ли такая таблица если нет со создаст таблицу"""
cur.execute("""CREATE TABLE IF NOT EXISTS table_couch(  
            id SERIAL PRIMARY KEY, 
            user_text VARCHAR(250),
            user_text2 TEXT,
            int_user INT
)""")


# cur.execute("""INSERT INTO table_couch (user_text, user_text2, int_user) VALUES ('Рандом текст ограничен', 'Неограничен', 1997)""") #пример добавления  только одного елемента в таблицу синтаксис:INSERT INTO table_name(values) VALUES(your_values)
# cur.execute("""INSERT INTO table_couch (user_text, user_text2, int_user) VALUES ('1_te', '1_te', 1997), ('1_te', '1_te', 1997), ('1_te', '1_te', 1997)""") #пример добавления нескольких елементов в таблицу, крайне удобен за счет того что не надо делать милион инсертов

# cur.execute("""DROP TABLE IF EXISTS table_couch""") # DROP TABLE - основная функция удаления таблицы, IF EXISTS table_name - эта приставка означает что мы будем удалять таблицу если она сущевствует

cur.execute("""SELECT user_text, int_user FROM table_couch""") #выбираем елементы из таблицы, синтаксис: SELECT elements FROM table_name, если хотите выбрать все елементы с таблицы:SELECT * FROM table_name
print(cur.fetchone()) #позволяет нам брать только один елемент 

# cur.execute("""SELECT user_text, user_text2, int_user FROM table_couch WHERE int_user BETWEEN 1997 AND 2022""") #тут мы можем создавать условия выборки, синтаксис:SELECT elements FROM table_name WHERE условие или другой вариант SELECT elements FROM table_name WHERE условие BETWEEN ____ AND ___ прямо говоря битвин помогает нам делать выборку по определенному радиусу


# print(cur.fetchall()) #берем все елементы из таблицы

# cur.execute("""ALTER TABLE table_couch ADD COLUMN new_column VARCHAR(50) """) #этот запрос помогает нам добавить новый столбец в таблицу синтаксис: ALTER TABLE table_name ADD COLUMN new_column type_column
# cur.execute("""INSERT INTO table_couch (new_column) VALUES ('HELLO')""") #добавляем информацию в столбец
# cur.execute("""ALTER TABLE table_couch DROP COLUMN new_column""") #этот запрос помогает нам удалить столбец из таблицы синтаксис: ALTER TABLE table_name DROP COLUMN column 
 
cur.execute(""" # поговорим про довольно актуальный метод кейс который используется вместе с селектом, в общем мы выбираем таблицу а потом делаем проверку инфы с столбца и если там какойто-такойто текст то мы создаем новую колонку и в ней будет записана информация
    SELECT 
        CASE 
            WHEN user_text = 'Рандом текст ограничен' THEN 'реально рандомный текст'
            ELSE user_text
        END AS text_group
    FROM table_couch
""")
"""синтаксис: SELECT
                CASE
                    WHEN element = inside_element THEN text_new_column
                    ELSE text_new_column
                END AS new_column
            FROM table_name
"""


"""Как удалять елементы с таблицы? это можно сделать с помощью запроса DELETE, синтаксис:DELETE FROM table_name WHERE situation  важно заметить что это удалит все елементы с этих столбцов, допустим я укажу в условии id = 1 и он удалит все данные связанные с первым айди"""

"""
   cur.execute(UPDATE table_couchs  SET int_user = 2020)
   cur.execute(UPDATE table_couchs  SET int_user = 1997 WHERE id = 1)
   эти два запроса помогают нам обновлять елементы столбцов, в первом варианте мы изменяем все инт юзеры  на значение 2020 а во второй ситуации мы делаем условие, если айдишка у нас равна одному то в этом слобце у нас заменится инт юзер на значение 1997
   синтаксис этого запроса: UPDATE table_name  SET value с условием: UPDATE table_name  SET value WHERE situation
"""

"""Так же мы можем сортировать данные с таблиц благодаря запросам ORDER BY, мы можем сортировать по нескольким критериям, таким как  DESC и ASC где первое по убыванию а второе по возврастанию 
примеры:
ORDER BY DESC
ORDER BY ASC
"""

print(cur.fetchall())

print(cur.fetchall())
# conn.commit() #записываем данные, да, так они не записуются поэтому надо самому

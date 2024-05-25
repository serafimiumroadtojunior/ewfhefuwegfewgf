import psycopg2 as pc

conn = pc.connect(
    host='',
    user='',  
    dbname='',
    password=''
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS table_couch( 
            id SERIAL PRIMARY KEY,
            user_text VARCHAR(250),
            user_text2 TEXT,
            int_user INT
)""")

# Inserting data into the table
# cur.execute("""INSERT INTO table_couch (user_text, user_text2, int_user) VALUES ('Рандом текст ограничен', 'Неограничен', 1997)""")
# cur.execute("""INSERT INTO table_couch (user_text, user_text2, int_user) VALUES ('1_te', '1_te', 1997), ('1_te', '1_te', 1997), ('1_te', '1_te', 1997)""")

# cur.execute("""DROP TABLE IF EXISTS table_couch""")

# Retrieving data from the table
cur.execute("""SELECT user_text FROM table_couch""")
print("All data:")
print(cur.fetchone())

# cur.execute("""SELECT user_text, user_text2, int_user FROM table_couch WHERE int_user BETWEEN 1997 AND 2022""")


# print("Data with id = 1:")
# print(cur.fetchall())

# Altering the table
# cur.execute("""ALTER TABLE table_couch ADD COLUMN new_column VARCHAR(50) """)
# cur.execute("""INSERT INTO table_couch (new_column) VALUES ('HELLO')""")
# cur.execute("""ALTER TABLE table_couch DROP COLUMN new_column""")

cur.execute("""
    SELECT 
        CASE 
            WHEN user_text = 'Рандом текст ограничен' THEN 'реально рандомный текст'
            ELSE user_text
        END AS text_group
    FROM table_couch
""")


print(cur.fetchall())

print(cur.fetchall())
conn.commit()

cur.close()
conn.close()

import psycopg2


# Подключение к базе данных
with psycopg2.connect(
    host = "localhost",
    database = "test",
    user= "postgres",
    password = "54242698"
) as conn:
    # Вызываем курсор, с помощью которого
    # мы выполняем опереации в базе данных
    with conn.cursor() as cur:
        # делаем запрос
        cur.execute("INSERT INTO post VALUES (%s, %s)", (8,"Hello my world",))
        cur.executemany("INSERT INTO post VALUES (%s, %s)",[(6,"Hello my world",),
                                                            (7,"Hello my world",)])
        cur.execute("SELECT * FROM post")
        # conn.commit()

        rows = cur.fetchall()
        # print(rows)

        for row in rows:
            print(row)


# закрываем курсор и соединение с базой данных
# cur.close()
conn.close()
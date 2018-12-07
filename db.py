import sqlite3


def init_db():
    conn = sqlite3.connect("bottom_price.sqlite")

    cursor = conn.cursor()

    with open("schema.sql")as f:
        sql = f.read()

    # sql = """CREATE TABLE products (
    #             name TEXT,
    #             price INTEGER,
    #             jan_code INTEGER
    #         )
    #         """

    cursor.executescript(sql)
    conn.commit()

    conn.close()


def find_all_products():
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM products;"

    products = cursor.execute(sql).fetchall()

    conn.commit()
    conn.close()
    return products


if __name__ == "__main__":
    init_db()
    print(find_all_products())
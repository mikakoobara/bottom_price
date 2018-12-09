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


def add_products(name, price, jan_code):
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO products (name, price, jan_code) VALUES (?, ?, ?)"
    cursor.execute(sql, (name, price, jan_code))

    conn.commit()
    conn.close()


def find_products(jan_code):
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM products WHERE jan_code = ?;"
    product = cursor.execute(sql, (jan_code,)).fetchone()

    conn.commit()
    conn.close()
    return product


def update_products(name, price, jan_code):
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "UPDATE products SET name = ?, price = ? WHERE  jan_code = ?;"
    cursor.execute(sql, (name, price, jan_code))

    conn.commit()
    conn.close()



if __name__ == "__main__":
    init_db()
    print(find_all_products())

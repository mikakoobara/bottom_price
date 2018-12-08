import sqlite3
import unittest


def get_product_name(jan_code):
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "SELECT name FROM products where jan_code = ?;"

    result = cursor.execute(sql, (jan_code,)).fetchone()

    products = result[0]

    conn.commit()
    conn.close()
    return products


def price(jan_code):
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "SELECT price FROM products where jan_code = ?;"
    result = cursor.execute(sql, (jan_code,)).fetchone()
    products = result[0]

    conn.commit()
    conn.close()
    return products


class TestBottomPrice(unittest.TestCase):
    def test_janコードを入力したら商品名が返ってくる(self):
        self.assertEqual("おーいお茶ほうじ茶", get_product_name(4901085176146))

    def test_janコードを入力したら金額が返ってくる(self):
        self.assertEqual(129, price(4901085176146))


if __name__ == "__main__":
    unittest.main()

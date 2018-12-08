import sqlite3
import unittest


def data(jan_code):
    conn = sqlite3.connect("bottom_price.sqlite")
    cursor = conn.cursor()

    sql = "SELECT name FROM products where jan_code = ?;"

    result = cursor.execute(sql, (jan_code,)).fetchone()

    products = result[0]

    conn.commit()
    conn.close()
    return products


class TestBottomPrice(unittest.TestCase):
    def test_janコードを入力したら商品名が返ってくる(self):
        self.assertEqual("おーいお茶ほうじ茶", data(4901085176146))


if __name__ == "__main__":
    unittest.main()

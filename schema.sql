-- schema.sql
DROP TABLE IF EXISTS products;

CREATE TABLE products (
  name TEXT,
  price INTEGER,
  jan_code INTEGER
);

-- サンプルデータを入れておく
INSERT INTO
  products
VALUES
  ('おーいお茶ほうじ茶', 129, 4901085176146),
  ('ぷるんと蒟蒻 イチゴ＋メロン', 216, 4571157255545)
;
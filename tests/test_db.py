def test_connection(db):
    assert db.connection is not None


def test_create_tables(db):
    db.create_table()
    result = db.select("SELECT name FROM sqlite_master WHERE type='table'")
    assert len(result) == 2
    assert "consumers" in [row[0] for row in result]
    assert "orders" in [row[0] for row in result]


def test_insert_consumer_and_order(db):
    db.create_table()

    # Insert a consumer
    db.execute("INSERT INTO consumers (name, age, city) VALUES ('Kate', 29, 'Chernivtsi')")
    consumer_result = db.select("SELECT * FROM consumers")
    assert len(consumer_result) == 1
    assert consumer_result[0][1] == 'Kate'
    assert consumer_result[0][2] == 29
    assert consumer_result[0][3] == 'Chernivtsi'

    # Insert an order for the consumer
    db.execute("INSERT INTO orders (human_id, item, quantity) VALUES (1, 'beer', 2)")
    order_result = db.select("SELECT * FROM orders")
    assert len(order_result) == 1
    assert order_result[0][1] == 1
    assert order_result[0][2] == 'beer'
    assert order_result[0][3] == 2

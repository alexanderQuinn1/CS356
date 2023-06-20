import database_connection as db


def get_product(prod_code):
    query = """
        SELECT * FROM product_type
        WHERE prod_type_code = %s;
    """

    results = db.fetch(query, (prod_code,))
    result = results[0]
    return {
        'product_code': prod_code,
        'product_name': result[1],
        'max_ph': result[2],
        'min_ph': result[3],
        'max_temp': result[4],
        'min_temp': result[5],
        'max_osmolality': result[6],
        'min_osmolality': result[7]
    }

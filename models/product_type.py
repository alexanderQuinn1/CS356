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
        'max_ph': result[1],
        'min_ph': result[2],
        'max_temp': result[3],
        'min_temp': result[4],
        'max_osmolality': result[5],
        'min_osmolality': result[6],
        'min_sterility': result[7]
    }

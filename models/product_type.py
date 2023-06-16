import database_connection as db

def get_product(prod_code):
    query = """
        SELECT * FROM product_type
        WHERE prod_type_code = %s;
    """

    results = db.fetch(query, (prod_code,))
    result = results[0]
    return {
        'prod_type_code': prod_code,
        'product_name': result[1],
        'min_temp': result[2],
        'max_temp': result[3],
        'min_ph': result[4],
        'max_ph': result[5],
        'min_osmolality': result[6],
        'max_osmolality': result[7]
    }

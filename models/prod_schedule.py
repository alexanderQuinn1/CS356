import database_connection as db


def get_by_prod_line(line):
    query = """
    SELECT prod_schedule_id , prod_line, activity_type 
    FROM miracle_cure_biotech.production_schedule
    WHERE start < now() AND end > NOW() AND prod_line = %s"""
    results = db.fetch(query, (line,))
    p = results[0]
    return {
        'prod_id': p[0],
        'prod_line': p[1],
        'activity_type': p[2]
    }

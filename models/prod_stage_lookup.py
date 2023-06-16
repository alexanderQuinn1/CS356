import database_connection as db


def get_all():
    query = """ SELECT * FROM miracle_cure_biotech.stage_lookup"""
    results = db.fetch(query)
    stages = []
    for result in results:
        stages.append({'id': result[0], 'name': result[1]})
    return stages

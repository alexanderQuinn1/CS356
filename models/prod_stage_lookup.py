import database_connection as db


def get_all():
    query = """ SELECT * FROM miracle_cure_biotech.stage_lookup"""
    results = db.fetch(query)
    stages = []
    for result in results:
        stages.append({'id': result[0], 'name': result[1]})
    return stages


def get(stage_id):
    query = """ SELECT * FROM miracle_cure_biotech.stage_lookup WHERE stage_id = %s"""
    results = db.fetch(query, (stage_id,))
    result = results[0]
    return {'id': result[0], 'name': result[1]}

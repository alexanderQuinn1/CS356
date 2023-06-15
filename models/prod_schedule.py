import database_connection as db
def get_current_prod_activity(line):
    return {
        'id': 4,
        'type': 'batch_manufacture'
    }

def get_prod_activities():
    query = """SELECT * FROM miracle_cure_biotech.production_schedule;"""

    results = db.execute_fetch(query)
    result = results[0]
    print(results)
    print(result)
    prod_activity_name = str(result[3]) + ' - ' + str(result[4])
    activities = {
        'title': prod_activity_name,
        'start': result[1],
        'end': result[2],
    }
    return activities

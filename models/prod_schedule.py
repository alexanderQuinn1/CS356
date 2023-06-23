import database_connection as db


def get_by_prod_line(line):
    return {
        'id': 4,
        'type': 'batch_manufacture'
    }


def insert(start, end, prod_line, activity_type):
    query = """
    INSERT INTO production_schedule (
    start,
    end,
    prod_line,
    activity_type)
    VALUES
    (%s, %s, %s, %s);
    """
    new_id = db.insert_commit(query, (start, end, prod_line, activity_type))
    return new_id


def get_all_prod_activities():
    query = """SELECT * FROM miracle_cure_biotech.production_schedule;"""

    results = db.commit(query)
    print(results)
    thislist = []
    for x in results:
        print(x)
        prod_activity_name = str(x[3]) + ' - ' + str(x[4])
        activities = {
            'title': prod_activity_name,
            'start': str(x[1]),
            'end': str(x[2]),
        }
        thislist.append(activities)
    return thislist


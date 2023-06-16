import database_connection as db


def get_current_prod_activity(line):
    return {
        'id': 4,
        'type': 'batch_manufacture'
    }

def add_batch_schedule():
    query = """
    """
    db.execute_insert(query)
def add_maintenance_schedule():
    query = """INSERT INTO `miracle_cure_biotech`.`maintenance_operation`
(`maintenance_id`,
`date`,
`plant_id`,
`description`,
`man_hours`,
`parts_replaced`,
`cost`,
`shutdown_required`,
`planned_activity`,
`prod_schedule_id`)
VALUES
(<{maintenance_id: }>,
<{date: }>,
<{plant_id: }>,
<{description: }>,
<{man_hours: }>,
<{parts_replaced: }>,
<{cost: }>,
<{shutdown_required: }>,
<{planned_activity: }>,
<{prod_schedule_id: }>);
"""
    db.execute_insert(query)

def add_prod_activity():
    query = """INSERT INTO `miracle_cure_biotech`.`production_schedule`
    (`prod_schedule_id`,
    `start`,
    `end`,
    `prod_line`,
    `activity_type`)
    VALUES
    (<{prod_schedule_id: }>,
    <{start: }>,
    <{end: }>,
    <{prod_line: }>,
    <{activity_type: }>);
    ;"""
    db.execute_insert(query)

def get_prod_activities():
    query = """SELECT * FROM miracle_cure_biotech.production_schedule;"""

    results = db.execute_fetch(query)
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

import database_connection as db


def get(batch_no, stage_id):
    query = """SELECT flask_monitor.flask_monitor_id, flask_monitor.temp, flask_monitor.ph, flask_monitor.osmoality
    FROM flask_monitor
    JOIN expansion ON flask_monitor.expansion_id = expansion.expansion_id
    WHERE expansion.stage = %s AND batch_id = %s
    """
    e = db.fetch(query, (stage_id, batch_no))
    return {
        'flasks': [
            {
                'id': e[0][0],
                'temp': e[0][1],
                'ph': e[0][2],
                'osmolality': e[0][3],
            },
            {
                'id': e[1][0],
                'temp': e[1][1],
                'ph': e[1][2],
                'osmolality': e[1][3],
            },
            {
                'id': e[2][0],
                'temp': e[2][1],
                'ph': e[2][2],
                'osmolality': e[2][3],
            },
            {
                'id': e[3][0],
                'temp': e[3][1],
                'ph': e[3][2],
                'osmolality': e[3][3],
            }
        ]
    }


def update(flask_monitor_id, temp, ph, osmolality):
    query = """UPDATE flask_monitor 
    SET flask_monitor.temp = %s, flask_monitor.ph = %s, flask_monitor.osmoality = %s
    WHERE flask_monitor.flask_monitor_id = %s
    """
    db.commit(query, (temp, ph, osmolality, flask_monitor_id))

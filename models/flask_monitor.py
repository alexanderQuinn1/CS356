import database_connection as db


def get(batch_no, stage_id):
    query = """select flask_monitor.flask_monitor_id, flask_monitor.temp, flask_monitor.ph, flask_monitor.osmoality
    from flask_monitor
    join expansion on flask_monitor.expansion_id = expansion.expansion_id
    where expansion.stage = %s and batch_id = %s
    """
    e = db.execute_fetch(query, (stage_id, batch_no))
    print(e)
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
    query = """update flask_monitor 
    set flask_monitor.temp = %s, flask_monitor.ph = %s, flask_monitor.osmoality = %s
    where flask_monitor.flask_monitor_id = %s
    """
    db.execute_update(query, (temp, ph, osmolality, flask_monitor_id))

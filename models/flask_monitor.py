import database_connection as db


def get_all(batch_no, stage_id):
    query = """
        SELECT flask_monitor.flask_monitor_id, flask_monitor.temp, flask_monitor.ph, flask_monitor.osmoality
        FROM flask_monitor
        JOIN expansion ON flask_monitor.expansion_id = expansion.expansion_id
        WHERE expansion.stage = %s AND batch_id = %s
    """

    results = db.fetch(query, (stage_id, batch_no))
    flasks = []
    for result in results:
        flasks.append({
            'id': result[0],
            'temp': result[1],
            'ph': result[2],
            'osmolality': result[3],
        })
    return flasks


def update(flask_monitor_id, temp, ph, osmolality):
    query = """
        UPDATE flask_monitor 
        SET flask_monitor.temp = %s, flask_monitor.ph = %s, flask_monitor.osmoality = %s
        WHERE flask_monitor.flask_monitor_id = %s
    """
    db.commit(query, (temp, ph, osmolality, flask_monitor_id))

import database_connection as db


def get_all(batch_no, stage_id):
    query = """
        SELECT 
            expansion.expansion_id, flask_monitor.flask_monitor_id, flask_monitor.temp, flask_monitor.ph, 
            flask_monitor.osmolality, flask_monitor.asset_id
        FROM flask_monitor
        JOIN expansion ON flask_monitor.expansion_id = expansion.expansion_id
        WHERE expansion.stage = %s AND batch_id = %s
    """

    results = db.fetch(query, (stage_id, batch_no))
    flasks = []
    for result in results:
        flasks.append({
            'id': result[1],
            'temp': result[2],
            'ph': result[3],
            'osmolality': result[4],
            'asset_id': result[5]
        })
    return {
        'expansion_id': results[0][0],
        'flasks': flasks
    }


def update(flask_monitor_id, temp, ph, osmolality):

    query = """
        UPDATE flask_monitor 
        SET flask_monitor.temp = %s, flask_monitor.ph = %s, flask_monitor.osmolality = %s
        WHERE flask_monitor.flask_monitor_id = %s
    """
    db.commit(query, (temp, ph, osmolality, flask_monitor_id))


def create(batch_no):
    create_expansion_query = """
            INSERT INTO expansion VALUES (%s, %s)
        """

    expansion1_id = db.insert_commit(create_expansion_query, (batch_no, 2))
    expansion2_id = db.insert_commit(create_expansion_query, (batch_no, 4))
    expansion3_id = db.insert_commit(create_expansion_query, (batch_no, 6))

    insert(expansion1_id)
    insert(expansion2_id)
    insert(expansion3_id)


def insert(expansion_id):
    create_flask_monitor_query = """
                    INSERT INTO flask_monitor VALUES (%s,0,0,0))
                """
    #TODO insert 4 seperate flask IDs once db changes merged
    db.insert_commit(create_flask_monitor_query, (expansion_id,))
    db.insert_commit(create_flask_monitor_query, (expansion_id,))
    db.insert_commit(create_flask_monitor_query, (expansion_id,))
    db.insert_commit(create_flask_monitor_query, (expansion_id,))
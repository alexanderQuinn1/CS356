import database_connection as db


def get(batch_no):
    query = """
        SELECT fill_room.fill_room_id, fill_room_monitor.fill_room_monitor_id, fill_room_monitor.humidity,  
            fill_room_monitor.last_stir_delta, fill_room_monitor.temp, fill_room_monitor.asset_id
        FROM fill_room_monitor
        JOIN fill_room ON fill_room_monitor.fill_room_id = fill_room.fill_room_id
        WHERE fill_room.batch_id = %s
    """

    results = db.fetch(query, (batch_no,))
    result = results[0]
    return {
        'fill_room_monitor_id': result[0],
        'fill_room_id': result[1],
        'humidity': result[2],
        'last_stir_delta': result[3],
        'temp': result[4],
        'asset_id': result[5]
    }


def update(fill_room_monitor_id, room_temp, humidity, last_stir_delta):
    query = """
        UPDATE fill_room_monitor 
        SET fill_room_monitor.humidity = %s, fill_room_monitor.last_stir_delta = %s, fill_room_monitor.temp = %s
        WHERE fill_room_monitor.fill_room_monitor_id = %s 
    """

    db.commit(query, (humidity, last_stir_delta, room_temp, fill_room_monitor_id))


def create(batch_no, fill_room_vat):
    create_fill_room_query = """
        INSERT INTO fill_room VALUES (default, %s)
    """

    fill_room_id = db.insert_commit(create_fill_room_query, (batch_no,))
    insert(fill_room_id, fill_room_vat)


def insert(fill_room_id, fill_room_vat):

    create_fill_room_monitor_query = """
                INSERT INTO fill_room_monitor VALUES (default, %s,0,0,0,%s)
            """

    db.insert_commit(create_fill_room_monitor_query, (fill_room_id, fill_room_vat))

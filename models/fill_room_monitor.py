import database_connection as db


def get(batch_no, stage_id):
    query = """
        SELECT fill_room.fill_room_id, fill_room_monitor.fill_room_monitor_id, fill_room_monitor.humidity,  fill_room_monitor.last_stir_delta, fill_room_monitor.temp 
        FROM fill_room_monitor
        JOIN fill_room ON fill_room_monitor.fill_room_id = fill_room.fill_room_id
        WHERE fill_room.stage = %s AND fill_room.batch_id = %s
    """

    results = db.fetch(query, (stage_id, batch_no))
    p = results[0]
    return {
        'fill_room_monitor_id': p[0],
        'fill_room_id': p[1],
        'humidity': p[2],
        'last_stir_delta': p[3],
        'temp': p[4],
        'asset_id': p[5]
    }


def update(fill_room_monitor_id, humidity, last_stir_delta, temp):
    query = """
        UPDATE fill_room_monitor 
        SET fill_room_monitor.humidity = %s, fill_room_monitor.last_stir_delta = %s, fill_room_monitor.temp = %s
        WHERE fill_room_monitor.fill_room_monitor_id = %s 
    """

    db.commit(query, (fill_room_monitor_id, humidity, last_stir_delta, temp))

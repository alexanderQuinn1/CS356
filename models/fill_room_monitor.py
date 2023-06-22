import database_connection as db


def get():
    query_stage = """SELECT fill_room.batch_id, fill_room_monitor.fill_room_monitor_id, fill_room_monitor.humidity, fill_room_monitor.last_stir_delta, fill_room_monitor.temp 
FROM miracle_cure_biotech.batch 
JOIN miracle_cure_biotech.fill_room on batch.batch_no = fill_room.batch_id
JOIN miracle_cure_biotech.fill_room_monitor  ON fill_room_monitor.fill_room_id = fill_room.fill_room_id
WHERE batch.current_stage = 8;"""
    results = db.fetch(query_stage)

    fill_rooms = []
    for result in results:
        fill_rooms.append({
            'batch': result[0],
            'id': result[1],
            'humidity': result[2],
            'last_stir_delta': result[3],
            'temp': result[4],
        })
    return fill_rooms


def get_all_current():
    # TODO get all currently in VATS

    return

def get_batchs_in_fillroom():
        query = """SELECT * FROM miracle_cure_biotech.batch  
            WHERE current_stage = 8;"""
        results = db.fetch(query)
        return


def update(batch_id):
    # TODO
    return



if __name__ == '__main__':
    get()

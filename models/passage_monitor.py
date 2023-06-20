import database_connection as db


def get(batch_no, stage_id):
    query = """
        SELECT passage.passage_id, passage_monitor.passage_id, passage_monitor.peristaltic_pump,  passage_monitor.cell_count 
        FROM passage_monitor
        JOIN passage ON passage_monitor.passage_id = passage.passage_id
        WHERE passage.stage = %s AND passage.batch_id = %s
    """

    results = db.fetch(query, (stage_id, batch_no))
    p = results[0]
    return {
        'passage_id': p[0],
        'monitor_id': p[1],
        'peristaltic_pump': p[2],
        'cell_count': p[3]
    }


def update(passage_monitor_id, peristaltic_pump, cell_count):
    query = """
        UPDATE passage_monitor 
        SET passage_monitor.peristaltic_pump = %s, passage_monitor.cell_count = %s
        WHERE passage_monitor.passage_monitor_id = %s 
    """

    db.commit(query, (peristaltic_pump, cell_count, passage_monitor_id))

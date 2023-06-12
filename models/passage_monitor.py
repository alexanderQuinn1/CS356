import database_connection as db


def get_passage_monitor(batch_no, stage_id):
    query = """ Select  passage_monitor.passage_id, passage_monitor.peristaltic_pump,  passage_monitor.cell_count from  passage_monitor
    JOIN passage  ON passage_monitor.passage_monitor_id = passage.passage_id
    WHERE passage.stage = %s and passage.batch_id = %s"""

    results = db.execute_fetch(query, (stage_id, batch_no))
    p = results[0]
    return {
                'id': p[0],
                'peristaltic_pump': p[1],
                'cell_count': p[2]
    }

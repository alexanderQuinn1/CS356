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


def create(batch_no):
    create_passage_query = """
        INSERT INTO passage VALUES (%s, %s)
    """

    passage1_id = db.insert_commit(create_passage_query, (batch_no, 3))
    passage2_id = db.insert_commit(create_passage_query, (batch_no, 5))
    end_of_line_id = db.insert_commit(create_passage_query, (batch_no, 7))

    insert(passage1_id)
    insert(passage2_id)
    insert(end_of_line_id)


def insert(passage_id):
    create_passage_monitor_query = """
                INSERT INTO passage_monitor VALUES (%s, 0, 'off'))
            """

    db.insert_commit(create_passage_monitor_query, (passage_id,))
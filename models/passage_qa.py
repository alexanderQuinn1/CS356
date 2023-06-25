import database_connection as db


def get(batch_no, stage_id):
    query = """
        SELECT * FROM passage_qa
        JOIN passage ON passage_qa.passage_id = passage.passage_id
        WHERE passage.batch_id = %s AND passage.stage = %s 
    """

    results = db.fetch(query, (batch_no, stage_id))

    if len(results) == 0:
        return None


    result = results[0]
    return {
        'passage_qa_id': result[0],
        'passage_id': result[1],
        'datetime': result[2],
        'cell_count': result[3],
        'ph': result[4],
        'osmolality': result[5],
        'sterility': result[6],
        'passed': result[7],
        'analysis': result[8]
    }


def insert(passage_id, date_time, cell_count, ph, osmolality, sterility, passed, analysis):
    query = """ 
        INSERT INTO passage_qa (passage_id, date_time, cell_count, ph, osmolality, sterility, passed, analysis)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
        """

    db.commit(query, (passage_id, date_time, cell_count, ph, osmolality, sterility, passed, analysis))

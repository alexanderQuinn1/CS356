import database_connection as db


def get(batch_no, stage_id):
    query = """
        SELECT * FROM fill_room_qa
        JOIN fill_room ON fill_room_qa.fill_room_id = fill_room.fill_room_id
        WHERE fill_room.batch_id = %s AND fill_room.stage = %s 
    """

    results = db.fetch(query, (batch_no, stage_id))

    if len(results) == 0:
        return None

    result = results[0]
    return {
        'fill_room_qa_id': result[0],
        'fill_room_id': result[1],
        'datetime': result[2],
        'mycoplasma': result[3],
        'virus_testing': result[4],
        'amino_acids': result[5],
        'trace_elements': result[6],
        'cell_count': result[7],
        'osmolality': result[8],
        'sterility': result[9],
        'passed': result[10],
        'analysis': result[11]
    }


def insert(fill_room_id, date_time, mycoplasma, virus_testing, amino_acids, trace_elements, cell_count, ph, osmolality,
           sterility, passed, analysis):
    query = """ 
        INSERT INTO fill_room_qa 
        (fill_room_id, date_time, mycoplasma, virus_testing, amino_acids, trace_elements, cell_count, ph, osmolality, 
        sterility, passed, analysis)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

    db.commit(query, (
        fill_room_id, date_time, mycoplasma, virus_testing, amino_acids, trace_elements, cell_count, ph, osmolality,
        sterility, passed, analysis))

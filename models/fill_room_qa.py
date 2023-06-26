import database_connection as db


def get(batch_no):
    query = """
        SELECT fill_room_qa.fill_room_qa_id, fill_room_qa.fill_room_id, fill_room_qa.mycoplasma, 
            fill_room_qa.virus_testing, fill_room_qa.amino_acids, fill_room_qa.trace_elements,
             fill_room_qa.cell_count, fill_room_qa.osmolality, fill_room_qa.sterility, fill_room_qa.passed, fill_room_qa.analysis
        FROM fill_room_qa
        JOIN fill_room ON fill_room_qa.fill_room_id = fill_room.fill_room_id
        WHERE fill_room.batch_id = %s;
    """

    results = db.fetch(query, (batch_no,))

    if len(results) == 0:
        return None

    result = results[0]
    return {
        'fill_room_qa_id': result[0],
        'fill_room_id': result[1],
        'mycoplasma': result[2],
        'virus_testing': result[3],
        'amino_acids': result[4],
        'trace_elements': result[5],
        'cell_count': result[6],
        'osmolality': result[7],
        'sterility': result[8],
        'passed': result[9],
        'analysis': result[10]
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

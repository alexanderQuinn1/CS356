import database_connection as db


def insert(form):
    # TODO
    # validate prod line doesnt have another batch scheduled simultaneously
    # prod_end = start_time + prod_duration
    # batch_no = IRVyymm9999
    return 'batch IRVyymm9999 scheduled'


def get(batch_no):
    query = """
        SELECT * FROM miracle_cure_biotech.batch  
        WHERE batch_no = %s ;
    """

    results = db.fetch(query, (batch_no,))
    result = results[0]
    return {
        'batch_no': batch_no,
        'quantity': result[1],
        'prod_type': result[2],
        'active_stage_id': result[4],
        'prod_schedule_id': result[5]
    }


def get_by_prod_schedule(prod_schedule_id):
    query = """
        SELECT * FROM miracle_cure_biotech.batch  
        WHERE prod_schedule_id = %s ;
    """

    results = db.fetch(query, (prod_schedule_id,))
    result = results[0]
    return {
        'batch_no': result[0],
        'quantity': result[1],
        'prod_type': result[2],
        'active_stage_id': result[4],
        'prod_schedule_id': prod_schedule_id
    }


def get_in_fill_room():
    query = """
        SELECT batch_no FROM miracle_cure_biotech.batch  
        WHERE current_stage = 8;
    """

    results = db.fetch(query)
    batch_numbers = []

    for result in results:
        batch_numbers.append(result[0])
    return batch_numbers


def update_stage(batch_no, stage_id):
    query = """
        UPDATE miracle_cure_biotech.batch
        SET current_stage = %s
        WHERE batch_no = %s;
    """

    db.commit(query, (stage_id, batch_no))

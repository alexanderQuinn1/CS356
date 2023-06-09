import database_connection as db


def insert(batch_no, prod_type_code, quantity, prod_sched_id):
    query = """
            INSERT INTO batch VALUES (%s,%s,%s,1,%s)
        """

    db.insert_commit(query, (batch_no, quantity, prod_type_code, prod_sched_id))


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
        'active_stage_id': result[3],
        'prod_schedule_id': result[4],
    }


def get_by_prod_schedule(prod_schedule_id):
    query = """
        SELECT * FROM miracle_cure_biotech.batch  
        WHERE prod_schedule_id = %s ;
    """

    results = db.fetch(query, (prod_schedule_id,))

    if(len(results) == 0):
        return None

    result = results[0]
    return {
        'batch_no': result[0],
        'quantity': result[1],
        'prod_type': result[2],
        'active_stage_id': result[3],
        'prod_schedule_id': prod_schedule_id,
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
        UPDATE batch
        SET current_stage = %s
        WHERE batch_no = %s;
    """

    db.commit(query, (stage_id, batch_no))


def get_latest_batch():
    query = """
        SELECT * FROM miracle_cure_biotech.batch ORDER BY batch_no DESC;
    """
    results = db.fetch(query)
    result = results[0]
    return {
        'batch_no': results[0][0]
    }


def get_batch_by_date(year, month):
    search_for = "IRV{0}{1}%".format(year, month)
    query = """
        SELECT * FROM miracle_cure_biotech.batch WHERE batch_no LIKE %s ORDER BY batch_no DESC;
    """
    results = db.fetch(query, (search_for,))
    if len(results) == 0:
        return None
    else:
        result = results[0]
        return result[0]


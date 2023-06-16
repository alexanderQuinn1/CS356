import database_connection as db


def schedule_batch(form):
    print(form)
    # validate prod line doesnt have another batch scheduled simultaneously
    # prod_end = start_time + prod_duration
    # batch_no = IRVyymm9999
    return 'batch IRVyymm9999 scheduled'


def get_batch_by_prod_schedule(prod_schedule_id):
    query = """SELECT * FROM miracle_cure_biotech.batch  
        WHERE prod_schedule_id = %s ;"""

    results = db.fetch(query, (prod_schedule_id,))
    result = results[0]
    return {
        'batch_no': result[0],
        'prod_type': result[2],
        'current_stage': result[4],
    }


def update_batch_stage(batch_no, stage_id):
    query = """UPDATE miracle_cure_biotech.batch
    SET current_stage = %s    
    WHERE batch_no= %s ;"""

    db.commit(query, (stage_id, batch_no))

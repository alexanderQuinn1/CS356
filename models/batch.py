import database_connection as db


def schedule_batch(form):
    print(form)
    # validate prod line doesnt have another batch scheduled simultaneously
    # prod_end = start_time + prod_duration
    # batch_no = IRVyymm9999
    return 'batch IRVyymm9999 scheduled'


def get_batch_in_production(prod_schedule_id):
    return {
        'batch_no': 'IRV2305001',
        'prod_type': 'XXXX99',
        'current_stage': 4,
    }


def update_batch_stage(batch_no, stage_id):
    query = """UPDATE miracle_cure_biotech.batch
    SET current_stage = %s    
    WHERE batch_no= %s ;"""

    print(batch_no)
    print(stage_id)
    db.execute_update(query, (stage_id, batch_no))

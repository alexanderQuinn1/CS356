import database_connection as db


def get_all_stages_based_on_step(current_stage_id):
    query = """ SELECT * FROM miracle_cure_biotech.stage_lookup"""
    results = db.execute_fetch(query)
    stages = []
    for result in results:
        stage_id = result[0]
        name = result[1]
        status = __get_status(stage_id, name, current_stage_id)
        stages.append({'id': stage_id, 'name': name, 'status': status})
    return stages


def get_stage_type(stage_id):
    if stage_id == 1:
        return 'start'
    elif stage_id == 2 or stage_id == 4 or stage_id == 6:
        return 'expansion'
    elif stage_id == 3 or stage_id == 5 or stage_id == 7:
        return 'passage'
    elif stage_id == 8:
        return 'fill_room'
    else:
        return 'complete'


def __get_status(stage_id, name, current_stage_id):
    if stage_id == current_stage_id:
        return 'active'
    elif stage_id < current_stage_id:
        return 'complete'
    elif stage_id == current_stage_id + 1:
        return 'next'
    elif stage_id > current_stage_id:
        return 'disabled'


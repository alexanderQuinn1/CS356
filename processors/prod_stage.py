import models.prod_stage_lookup as prod_stage_lookup_repo


def get_stepper_config(batch):
    stages = prod_stage_lookup_repo.get_all()
    for stage in stages:
        stage['status'] = __get_status(stage['id'], stage['name'], batch)
    return stages


def get_stage_name(stage_id):
    stage = prod_stage_lookup_repo.get(stage_id)
    if stage:
        return stage['name']


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


def __get_status(stage_id, name, batch):
    active_stage_id = batch['active_stage']['id']

    # TODO tidy up
    qa_failed = None
    if 'qa' in batch['active_stage']['data'] and batch['active_stage']['data']['qa'] is not None:
        qa_failed = not batch['active_stage']['data']['qa']['passed']

    if stage_id == active_stage_id:
        return 'active' if not qa_failed else 'error'
    elif stage_id < active_stage_id:
        return 'complete'
    elif stage_id == active_stage_id + 1:
        return 'next' if not qa_failed else 'disabled'
    elif stage_id > active_stage_id:
        return 'disabled'

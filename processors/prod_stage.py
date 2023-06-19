import models.prod_stage_lookup as prod_stage_lookup_repo


def get_display_stages(active_stage_id):
    stages = prod_stage_lookup_repo.get_all()
    for stage in stages:
        stage['status'] = __get_status(stage['id'], stage['name'], active_stage_id)
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


def __get_status(stage_id, name, active_stage_id):
    if stage_id == active_stage_id:
        return 'active'
    elif stage_id < active_stage_id:
        return 'complete'
    elif stage_id == active_stage_id + 1:
        return 'next'
    elif stage_id > active_stage_id:
        return 'disabled'


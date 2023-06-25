import models.prod_stage_lookup as prod_stage_lookup_repo


def get_monitoring_stages(active_stage_id):
    stages = prod_stage_lookup_repo.get_all()
    monitoring_stages = list(filter(__is_monitoring_stage, stages))

    for stage in monitoring_stages:
            stage['status'] = __get_status(stage['id'], active_stage_id)
    return monitoring_stages


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


def __get_status(stage_id, active_stage_id):
    if stage_id == active_stage_id:
        return 'active'
    elif stage_id < active_stage_id:
        return 'complete'
    elif stage_id == active_stage_id + 1:
        return 'next'
    elif stage_id > active_stage_id:
        return 'disabled'


def __is_monitoring_stage(x):
    stage_type = get_stage_type(x['id'])
    if stage_type == 'fill_room' or stage_type == 'complete':
        return False
    else:
        return True


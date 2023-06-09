def get_all_stages_based_on_step(current_stage_id):
    stages = [
        {'id': 1, 'name': 'start'},
        {'id': 2, 'name': 'expansion 1'},
        {'id': 3, 'name': 'Passage 1'},
        {'id': 4, 'name': 'Expansion 2'},
        {'id': 5, 'name': 'Passage 2'},
        {'id': 6, 'name': 'Expansion 3'},
        {'id': 7, 'name': 'End of Line'},
    ]
    for stage in stages:
        stage['status'] = __get_status(stage, current_stage_id)
    return stages


def get_stage_type(stage_id):
    if stage_id == 2 or stage_id == 4 or stage_id == 6:
        return 'expansion'
    elif stage_id == 3 or stage_id == 5 or stage_id == 7:
        return 'passage'
    else:
        return 'start'


def __get_status(stage, current_stage_id):
    if stage['id'] == current_stage_id:
        return 'active'
    elif stage['id'] < current_stage_id:
        return 'complete'
    elif stage['id'] == current_stage_id + 1:
        return 'next'
    elif stage['id'] > current_stage_id:
        return 'disabled'


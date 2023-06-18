from datetime import datetime
import models.passage_qa as passage_qa_repo
import models.passage_monitor as passage_monitor_repo


def add_qa(form, batch):
    failures = __analyse_results(batch['product'], form['ph'], form['osmolality'], form['sterility'])
    passed = __has_passed(failures)
    passage_id = batch['active_stage']['data']['passage']['passage_id']
    passage_qa_repo.insert(passage_id, datetime.now(), form['cell_count'], form['ph'], form['osmolality'],
                           form['sterility'], passed)
    return None


def update_monitor(form, batch):
    passage_id = batch['active_stage']['data']['passage']['monitor_id']
    passage_monitor_repo.update(passage_id, form['peristaltic_pump'], form['cell_count'])
    return None


def get_qa(batch_no, stage_id):
    qa = passage_qa_repo.get(batch_no, stage_id)
    qa['result'] = 'passed' if qa['passed'] else 'failed'
    qa['colour'] = 'green' if qa['passed'] else 'red'
    return qa


def __analyse_results(product, ph, osmolality, sterility):
    # TODO
    failures = []
    if ph < product['min_ph']:
        failures.append('sample is too acidic')
    return failures


def __has_passed(failures):
    return failures.len() == 0

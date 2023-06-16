import models.batch as batch_repo
import models.flask_monitor as flask_monitor_repo
import models.passage_monitor as passage_monitor_repo
import processors.passage as passage_processor


def get_batch(batch_no):
    batch = batch_repo.get(batch_no)
    return __create_batch_obj(batch)


def get_batch_by_prod_schedule(prod_schedule_id):
    pbatch = batch_repo.get_by_prod_schedule(prod_schedule_id)
    return __create_batch_obj(batch)


def update_batch_stage(batch_no, current_stage_id):
    stage_id = int(current_stage_id) + 1
    batch_repo.update_batch_stage(batch_no, stage_id)


def __create_batch_obj(batch):
    f = flask_monitor_repo.get(b['batch_no'], b['current_stage'])
    p = passage_monitor_repo.get(b['batch_no'], b['current_stage'])
    qa = passage_processor.get_qa_results(p['id'])

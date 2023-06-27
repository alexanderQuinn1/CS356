from datetime import datetime
import models.passage_qa as passage_qa_repo
import models.passage_monitor as passage_monitor_repo
import processors.qa as qa_processor


def add_qa(form, batch):
    cell_count = int(form['cell_count'])
    ph = int(form['ph'])
    osmolality = int(form['osmolality'])
    sterility = int(form['sterility'])
    passage_id = batch['active_stage']['data']['passage']['passage_id']

    failures = qa_processor.analyse_results(batch['product'], ph, osmolality, sterility)
    analysis = qa_processor.analysis_to_string(failures)
    passed = qa_processor.has_failures(failures)

    passage_qa_repo.insert(passage_id, datetime.now(), cell_count, ph, osmolality,
                           sterility, passed, analysis)


def update_monitor(form, batch):
    peristaltic_pump = form['peristaltic_pump']
    cell_count = int(form['cell_count'])
    passage_id = batch['active_stage']['data']['passage']['monitor_id']

    passage_monitor_repo.update(passage_id, peristaltic_pump, cell_count)


def get_qa(batch_no, stage_id):
    qa = passage_qa_repo.get(batch_no, stage_id)
    qa_processor.add_qa_details(qa)
    return qa


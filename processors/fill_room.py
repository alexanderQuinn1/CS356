from datetime import datetime
import models.fill_room_qa as fill_room_qa_repo
import models.fill_room_monitor as fill_room_monitor_repo
import processors.qa as qa_processor
import models.batch as batch_repo
import processors.batch as batch_processor


def add_qa(form, batch):
    cell_count = int(form['cell_count'])
    ph = int(form['ph'])
    osmolality = int(form['osmolality'])
    sterility = int(form['sterility'])
    mycoplasma = form['mycoplasma']
    virus_testing = form['virus_testing']
    amino_acids = form['amino_acids']
    trace_elements = form['trace_elements']
    fill_room_id = batch['active_stage']['data']['fill_room']['fill_room_id']

    failures = __analyse_results(batch['product'], ph, osmolality, sterility, mycoplasma, virus_testing, amino_acids,
                                 trace_elements)
    analysis = qa_processor.analysis_to_string(failures)

    passed = qa_processor.has_failures(failures)

    fill_room_qa_repo.insert(fill_room_id, datetime.now(), mycoplasma, virus_testing, amino_acids, trace_elements,
                             cell_count, ph, osmolality,
                             sterility, passed, analysis)


def update_monitor(form, batch):
    room_temp = int(form['room_temp'])
    humidity = int(form['humidity'])
    last_stir_delta = int(form['last_stir_delta'])
    fill_room_monitor_id = batch['active_stage']['data']['fill_room']['fill_room_monitor_id']

    fill_room_monitor_repo.update(fill_room_monitor_id, room_temp, humidity, last_stir_delta)


def __analyse_results(product, ph, osmolality, sterility, mycoplasma, virus_testing, amino_acids, trace_elements):
    failures = qa_processor.analyse_results(product, ph, osmolality, sterility)

    if mycoplasma != "favourable":
        failures.append('Mycoplasma is not favourable: batch should be disposed')
    if virus_testing != "favourable":
        failures.append('Virus testing is not favourable: batch should be disposed')
    if amino_acids != "favourable":
        failures.append('Amino acids are not favourable: batch should be disposed')
    if trace_elements != "favourable":
        failures.append('Trace elements are not favourable: batch should be disposed')

    return failures


def get_batches_in_fill_room():
    batch_numbers = batch_repo.get_in_fill_room()
    batches = []
    for batch_no in batch_numbers:
        batches.append(batch_processor.get_batch(batch_no))
    return batches


def get_qa(batch_no):
    qa = fill_room_qa_repo.get(batch_no)
    qa_processor.add_qa_details(qa)
    return qa

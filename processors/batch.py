import models.batch as batch_repo
import models.product_type as product_type_repo
import models.flask_monitor as flask_monitor_repo
import models.passage_monitor as passage_monitor_repo
import models.fill_room_monitor as fill_room_monitor_repo
import processors.passage as passage_processor
import processors.prod_stage as prod_stage_processor
import processors.fill_room as fill_room_processor


def get_batch(batch_no):
    batch = batch_repo.get(batch_no)
    return __map_batch_obj(batch)


def get_batch_by_prod_schedule(prod_schedule_id):
    batch = batch_repo.get_by_prod_schedule(prod_schedule_id)
    return __map_batch_obj(batch)


def update_stage(batch_no):
    batch = get_batch(batch_no)
    current_stage_id = batch['active_stage']['id']
    stage_id = int(current_stage_id) + 1
    batch_repo.update_stage(batch_no, stage_id)


def add_batch_padding(padding, new_batch_digit):
    length = new_batch_digit
    length_after = padding
    new_string = '0' * (length_after - len(str(length))) + str(length)
    return new_string


def generate_batch_number(start_date):
    lastest_batch_no = batch_repo.get_batch_by_date(start_date.year, start_date.month)
    if lastest_batch_no is None:
        month = add_batch_padding(2, start_date.month)
        batch_string = 'IRV{0}{1}001'.format(str(start_date.year), month)
    else:
        last_digits = int(lastest_batch_no[-3])
        new_batch_digit = last_digits + 1
        padded_digit = add_batch_padding(3, new_batch_digit)
        month = add_batch_padding(2, start_date.month)
        batch_string = 'IRV{0}{1}{2}'.format(str(start_date.year), month, padded_digit)
    return batch_string


def create_new_batch(batch_no, prod_type, quantity, prod_sched_id, fill_room_vat):
    batch_repo.insert(batch_no, prod_type, quantity, prod_sched_id)
    passage_monitor_repo.create(batch_no)
    flask_monitor_repo.create(batch_no)
    fill_room_monitor_repo.create(batch_no, fill_room_vat)


def __map_batch_obj(batch):
    product = product_type_repo.get_product(batch['prod_type'])
    stage_type = prod_stage_processor.get_stage_type(batch['active_stage_id'])

    return {
        'batch_no': batch['batch_no'],
        'quantity': batch['quantity'],
        'product': product,
        'active_stage': {
            'id': batch['active_stage_id'],
            'type': stage_type,
            'name': prod_stage_processor.get_stage_name(batch['active_stage_id']),
            'data': __get_stage_data(stage_type, batch)
        }
    }


def __get_stage_data(stage_type, batch):
    if stage_type == 'expansion':
        data = flask_monitor_repo.get_all(batch['batch_no'], batch['active_stage_id'])
        return {'expansion': data}
    elif stage_type == 'passage':
        passage = passage_monitor_repo.get(batch['batch_no'], batch['active_stage_id'])
        qa = passage_processor.get_qa(batch['batch_no'], batch['active_stage_id'])
        return {
            'passage': passage,
            'qa': qa
        }
    elif stage_type == 'fill_room':
        fill_room = fill_room_monitor_repo.get(batch['batch_no'])
        qa = fill_room_processor.get_qa(batch['batch_no'])
        return {
            'fill_room': fill_room,
            'qa': qa
        }

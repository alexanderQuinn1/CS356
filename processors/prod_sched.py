from datetime import datetime,timedelta
import models.prod_schedule as prod_schedule_repo
import models.maintenance_operation as maintenance_operation_repo
import processors.batch as batch_processor


def schedule_activity(form):
    prod_line = form['prod_line']
    activity_type = form['prod_activity_type']

    start = datetime.strptime(form['start'], '%Y-%m-%dT%H:%M')
    duration = int(form['duration'])
    end = calculate_end_time(start, duration)

    # TODO
    # return form validation if there is a production activity going on
    # if prod_sched has activity that starts after start and before end or has activity that ends after start or before end and prod_line = prod_line

    prod_sched_id = prod_schedule_repo.insert(start, end, prod_line, activity_type)

    if activity_type == 'maintenance':
        plant_id = form['plant_id']
        description = form['work_description']
        parts_replaced = form['parts_replaced']
        cost = float(form['parts_cost'])
        shutdown_required = form['shutdown_required']
        planned = form['planned']

        maintenance_operation_repo.insert(plant_id, description, duration, parts_replaced, cost, shutdown_required,planned, prod_sched_id)

    elif activity_type == 'batch':
        prod_type = form['prod_type_code']
        quantity = int(form['quantity'])
        vat_id = form['fill_room_vat_id']
        batch_no = batch_processor.generate_batch_number(start)

        batch_processor.create_new_batch(batch_no, prod_type, quantity, prod_sched_id, vat_id)


def formatted_events():
    events = prod_schedule_repo.get_all_prod_activities()
    return events


def calculate_end_time(start, duration):
    end_time = start + timedelta(hours=duration)
    return end_time


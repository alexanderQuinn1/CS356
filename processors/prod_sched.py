from datetime import datetime,timedelta
import models.prod_schedule as prod_schedule_repo
import models.batch as batch_repo
import models.maintenance_operation as maintenance_operation_repo
import arrow


def schedule_activity(form):
    prod_line = form['prod_line']
    activity_type = form['prod_activity_type']

    start = datetime.strptime(form['start'], '%Y-%m-%dT%H:%M')
    duration = int(form['duration'])
    end = calculate_end_time(start, duration)

    # TODO
    # return form validation if there is a production activity going on
    # if prod_sched has activity that starts after start and before end or has activity that ends after start or before end and prod_line = prod_line

    prod_id = prod_schedule_repo.insert(start, end, prod_line, activity_type)
    print(prod_id)

    if type == 'maintenance':

        maintenance_operation_repo.insert()

    elif type == 'batch manufacture':
        prod_type = form['prod_type']
        quantity = form['quantity']
        batch_repo.insert()


def formatted_events():
    events = prod_schedule_repo.get_all_prod_activities()
    return events


def calculate_end_time(start, duration):
    end_time = start + timedelta(hours=duration)
    return end_time


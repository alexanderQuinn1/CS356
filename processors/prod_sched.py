from datetime import datetime,timedelta
import models.prod_schedule as prod_schedule_repo
import models.batch as batch_repo
import models.maintenance_operation as maintenance_operation_repo


def schedule_activity(form):
    prod_line = form['prod_line']
    type = form['prod_activity_type']

    start = datetime.strptime(form['start'], '%m/%d/%y %H:%M')
    duration = int(form['duration'])
    end = calculate_end_time(start, duration)

    # TODO
    # return form validation if there is a production activity going on

    prod_id = prod_schedule_repo.insert(start, end, )

    if type == 'maintenance':
        maintenance_operation_repo.insert()

    elif type == 'batch manufacture':
        batch_repo.insert()


def calculate_end_time(start, duration):
    return start + timedelta(hours=duration)


from flask import render_template
import models.product_type as product_type
import models.flask_monitor as flask_monitor
import models.passage_monitor as passage_monitor
import models.passage_qa as passage_qa
import models.prod_schedule as prod_schedule
import models.batch as batch
import models.prod_stage_lookup as prod_stage_lookup
import models.prod_schedule as prod_sched
from flask import json



def render_prod_activity(heading, prod_line):
    prod_activity = prod_schedule.get_current_prod_activity(prod_line)
    if prod_activity['type'] == 'batch_manufacture':
        return render_batch_manufacture(heading, prod_line, prod_activity)
    elif prod_activity['type'] == 'maintenance':
        # TODO
        return None
    else:
        # TODO
        return None


def render_batch_manufacture(heading, prod_line, prod_activity):
    b = batch.get_batch_by_prod_schedule(prod_activity['id'])
    product = product_type.get_product(b['prod_type'])
    stages = prod_stage_lookup.get_all_stages_based_on_step(b['current_stage'])

    stage_type = prod_stage_lookup.get_stage_type(b['current_stage'])

    if stage_type == 'expansion':
        f = flask_monitor.get_flask_monitor(b['batch_no'], b['current_stage'])
        return render_template('prod-line-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=b, expansion_monitor=f, product=product)
    elif stage_type == 'passage':
        p = passage_monitor.get(b['batch_no'], b['current_stage'])
        qa = passage_qa.get_qa_outcome(p['id'])
        return render_template('prod-line-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=b, passage_monitor=p, passage_qa=qa, product=product)
    else:
        return render_template('prod-line-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=b)


def render_batch_monitor_entry(heading, entry_type):
    return render_template('maintenance-batch-entry.html', heading=heading, entry_type=entry_type)


def update_batch_stage(batch_no, current_stage_id):
    stage_id = int(current_stage_id) + 1
    batch.update_batch_stage(batch_no, stage_id)

def render_prod_schedule_calender(heading):
    p = prod_sched.get_prod_activities()
    return render_template('prod-line-schedule.html', heading=heading, prod_activity=json.dumps(p))

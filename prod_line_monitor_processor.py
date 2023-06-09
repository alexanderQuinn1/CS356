from flask import render_template
import models.product_type as product_type
import models.flask_monitor as flask_monitor
import models.passage_monitor as passage_monitor
import models.passage_qa as passage_qa


def render_prod_activity(heading, prod_line):
    prod_activity = {
        'type': 'batch_manufacture'
    }
    if prod_activity['type'] == 'batch_manufacture':
        return render_batch_manufacture(heading, prod_line)
    elif prod_activity['type'] == 'maintenance':
        # TODO
        return None
    else:
        # TODO
        return None


def render_batch_manufacture(heading, prod_line):
    # TODO get batch currently in production on prod_line from DB
    batch = {
        'batch_no': 'IRV99999999',
        'prod_type': 'XXXX99',
        'current_stage': 3,
    }
    product = product_type.get_product(batch['prod_type'])
    stages = [
        {'id': 1, 'name': 'start', 'status': 'complete'},
        {'id': 2, 'name': 'expansion 1', 'status': 'active'},
        {'id': 3, 'name': 'Passage 1', 'status': 'next'},
        {'id': 4, 'name': 'Expansion 2', 'status': 'disabled'},
        {'id': 5, 'name': 'Passage 2', 'status': 'disabled'},
        {'id': 6, 'name': 'Expansion 3', 'status': 'disabled'},
        {'id': 7, 'name': 'End of Line', 'status': 'disabled'},
    ]
    if batch['current_stage'] == 2 or batch['current_stage'] == 4 or batch['current_stage'] == 6:
        f = flask_monitor.get_flask_monitor(batch['batch_no'], batch['current_stage'])
        return render_template('prod-line-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=batch, expansion_monitor=f, product=product)
    elif batch['current_stage'] == 3 or batch['current_stage'] == 5 or batch['current_stage'] == 7:
        p = passage_monitor.get_passage_monitor(batch['batch_no'], batch['current_stage'])
        qa = passage_qa.get_qa_outcome(p['id'])
        return render_template('prod-line-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=batch, passage_monitor=p, passage_qa=qa, product=product)
    else:
        return render_template('prod-line-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=batch)

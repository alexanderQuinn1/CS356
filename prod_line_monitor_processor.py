from flask import render_template


def render_prod_activity(heading, prod_line):
    #TODO fetch prod activity from DB
    prod_activity = {
        'type': 'batch_manufacture'
    }
    if prod_activity['type'] == 'batch_manufacture':
        return render_batch_manufacture(heading, prod_line)
    elif prod_activity['type'] == 'maintenance':
        #TODO
        return None
    else:
        #TODO
        return None


def render_batch_manufacture(heading, prod_line):
    # TODO get batch currently in production on prod_line from DB
    b = {
        'batch_no': 'IRV99999999',
        'prod_type': 'x',
        'current_stage': 3,
    }
    if b['current_stage'] == 2 or b['current_stage'] == 4 or b['current_stage'] == 6:
        return render_expansion_monitor(heading, prod_line, b)
    elif b['current_stage'] == 3 or b['current_stage'] == 5 or b['current_stage'] == 7:
        return render_passage_monitor(heading, prod_line, b)
    else:
        #TODO show something if the stage is start
        return None


def render_expansion_monitor(heading, prod_line, batch):
        # TODO get operating params for the batch
        p = {
            'min_temp': 36,
            'max_temp': 38,
            'min_ph': 6,
            'max_ph': 8,
            'min_osmolality': 360,
            'max_osmolality': 420
        }
        # TODO get flask monitoring data for the current expansion
        m = {
            'flasks': [
                {
                    'id': 12345678,
                    'temp': 37,
                    'ph': 8.2,
                    'osmolality': 369,
                },
                {
                    'id': 12345679,
                    'temp': 35,
                    'ph': 7,
                    'osmolality': 369,
                },
                {
                    'id': 12345680,
                    'temp': 37,
                    'ph': 7,
                    'osmolality': 369,
                },
                {
                    'id': 123456790,
                    'temp': 37,
                    'ph': 7,
                    'osmolality': 369,
                }]
        }
        return render_template('expansion-monitor.html', heading=heading, prod_line=prod_line, batch=batch, monitor=m,
                               product=p)
    # do this for passage, todo: this should use ID's for passage 1 or 2 or end of line
    elif b['current_stage'] == 'passage':
        # get monitor
        m = {
            'peristaltic_pump': 'low',
            'cell_count': '1.63x10^9'
        }
        # get qa
        qa = {
            'status': 'pass',
            'colour': 'green'
        }
        return render_template('passage-monitor.html', heading=heading, prod_line=prod_line, batch=b, monitor=m, qa=qa)


def render_passage_monitor(heading, prod_line, batch):
    # TODO get passage monitoring data for the current passage
    m = {
        'peristaltic_pump': 'low',
        'cell_count': '1.63x10^9'
    }
    # TODO get qa for the current passage if any
    qa = None
    # qa = {
    #     'status': 'pass',
    #     'colour': 'green'
    # }
    return render_template('passage-monitor.html', heading=heading, prod_line=prod_line, batch=batch, monitor=m, qa=qa)

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
    # do this for expansion, todo: this should use ID's for expansion 1 or 2
    if b['current_stage'] == 'expansion':
        # get operating params
        p = {
            'min_temp': 36.5,
            'max_temp': 37.5
        }
        # get flask monitors
        m = {
            'flasks': [
                {
                    'id': 12345678,
                    'temp': 37,
                    'ph': 7,
                    'osmolality': 369,
                },
                {
                    'id': 12345679,
                    'temp': 37,
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
        return render_template('expansion-monitor.html', heading=heading, prod_line=prod_line, batch=b, monitor=m,
                               product=p)
    # do this for passage, todo: this should use ID's for passage 1 or 2 or end of line
    elif b['current_stage'] == 'passage':
        # get monitor
        m = {
            'peristaltic_pump': 'low',
            'cell_count': '1.63x10^9'
        }
        # get qa
        qa = None
        # qa = {
        #     'status': 'pass',
        #     'colour': 'green'
        # }
        return render_template('passage-monitor.html', heading=heading, prod_line=prod_line, batch=b, monitor=m, qa=qa)
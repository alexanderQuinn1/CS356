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
        'prod_type': 'XXXX99',
        'current_stage': 3,
    }
    if b['current_stage'] == 1 or b['current_stage'] == 3 or b['current_stage'] == 5:
        p = {
            'min_temp': 36.5,
            'max_temp': 37.5,
            'min_ph': 6.5,
            'max_ph': 7.5,
            'min_osmolality': 360,
            'max_osmolality': 420
        }
        m = {
            'flasks': [
                {
                    'id': 12345678,
                    'temp': 37,
                    'ph': 6,
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
                    'osmolality': 500,
                }]
        }
        return render_template('expansion-monitor.html', heading=heading, prod_line=prod_line, batch=b, monitor=m,
                               product=p)
    elif b['current_stage'] == 2 or b['current_stage'] == 4 or b['current_stage'] == 6:
        m = {
            'peristaltic_pump': 'low',
            'cell_count': '1.63x10^9'
        }
        qa = {
            'status': 'pass',
            'colour': 'green'
        }
        return render_template('passage-monitor.html', heading=heading, prod_line=prod_line, batch=b, monitor=m, qa=qa)
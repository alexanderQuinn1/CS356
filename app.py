import math

from flask import Flask, render_template, request
import database_connection as db
import models.batch as batch
import models.maintenance_operation as maintenance
import models.passage_qa as qa

app = Flask(__name__)


@app.route('/')
def run_app():
    return render_template('dashboard.html', heading='Management Dashboard')


@app.route('/prod-line-monitor', methods=['GET', 'POST'])
def run_production_line():
    # get production line
    pl = 'A'
    # get batch
    b = {
        'batch_id': 'IRV99999999',
        'prod_type': 'x',
        'current_stage': 'passage',
    }
    if request.method == 'GET':
        # do this for expansion, todo: this should use ID's for expansion 1 or 2
        if b['current_stage'] == 'expansion':
            # get operating params
            p = {
                'min_temp': 36.5,
                'max_temp': 37.5
            }
            # get flask monitors
            m = {
                'flaskA': {
                    'id'
                    'temp': 37,
                    'ph': 7,
                    'osmolality': 369,
                },
                'flaskB': {
                    'id'
                    'temp': 37
                },
                'flaskC': {
                    'id'
                    'temp': 37
                },
                'flaskD': {
                    'id'
                    'temp': 37
                }
            }
            return render_template('expansion-monitor.html', heading='Production Line Monitor', prod_line=pl, batch=b, monitor=m, product=p)
        # do this for passage, todo: this should use ID's for passage 1 or 2 or end of line
        elif b['current_stage'] == 'passage':
            # get monitor
            m = {
                'peristaltic_pump': 'low',
                'cell_count': 122777282828229828292
            }
            # get qa
            qa = None
            return render_template('passage-monitor.html', heading='Production Line Monitor', prod_line=pl, batch=b, monitor=m, qa_data=qa)


@app.route('/prod-schedule')
def run_production_schedule():
    return render_template('prod-line-schedule.html', heading="Production Schedule")


@app.route('/qa-log')
def run_quality_assurance():
    return render_template('qa-log.html', heading="Quality Assurance Log")


@app.route('/maintenance-log')
def run_maintenance_log():
    return render_template('maintenance-log.html', heading="Maintenance Log")


@app.route('/qa-entry', methods=['GET', 'POST'])
def run_quality_assurance_entry():
    if request.method == 'GET':
        return render_template('qa-entry.html')
    else:
        response = qa.save_qa(request.form)
        return render_template('qa-entry.html', response=response)


@app.route('/maintenance-entry', methods=['GET', 'POST'])
def run_maintenance_entry():
    if request.method == 'GET':
        return render_template('maintenance-entry.html')
    else:
        response = maintenance.save_maintenance_activity(request.form)
        return render_template('maintenance-entry.html', response=response)


@app.route('/batch-schedule-entry', methods=['GET', 'POST'])
def run_batch_schedule_entry():
    if request.method == 'GET':
        return render_template('batch-schedule-entry.html')
    else:
        response = batch.schedule_batch(request.form)
        return render_template('batch-schedule-entry.html', response=response)


if __name__ == '__main__':
    # db.create()
    app.run(debug=True, port=5001)

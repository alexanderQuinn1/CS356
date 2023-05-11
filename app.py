from flask import Flask, render_template, request
from maintenance import save_maintenance_activity
from productionSchedule import create_batch
import database_connection as db

app = Flask(__name__)


@app.route('/')
def run_app():
    return render_template('dashboard.html')


@app.route('/productionLine')
def run_production_line():
    return render_template('prod-line-monitor.html')


@app.route('/productionSchedule')
def run_production_schedule():
    return render_template('prod-line-schedule.html')


@app.route('/qualityAssurance')
def run_quality_assurance():
    return render_template('qa-log.html')


@app.route('/maintenanceLog')
def run_maintenance_log():
    return render_template('maintenance-log.html')


@app.route('/maintenanceEntry', methods=['GET', 'POST'])
def run_maintenance_entry():
    if request.method == 'GET':
        return render_template('maintenanc-entry.html')
    else:
        response = save_maintenance_activity(request.form)
        return render_template('maintenanc-entry.html', response=response)


@app.route('/batchScheduleEntry', methods=['GET', 'POST'])
def run_batch_schedule_entry():
    if request.method == 'GET':
        return render_template('batch-schedule-entry.html')
    else:
        response = create_batch(request.form)
        return render_template('batch-schedule-entry.html', response=response)


if __name__ == '__main__':
    db.create()
    app.run(debug=True, port=5001)

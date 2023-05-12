from flask import Flask, render_template, request
import database_connection as db
import models.batch as batch
import models.maintenance_operation as maintenance
import models.quality_assurance as qa

app = Flask(__name__)


@app.route('/')
def run_app():
    return render_template('dashboard.html', heading='Management Dashboard')


@app.route('/prod-line-monitor')
def run_production_line():
    return render_template('prod-line-monitor.html', heading='Production Line Monitor')


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
        return render_template('maintenanc-entry.html')
    else:
        response = maintenance.save_maintenance_activity(request.form)
        return render_template('maintenanc-entry.html', response=response)


@app.route('/batch-schedule-entry', methods=['GET', 'POST'])
def run_batch_schedule_entry():
    if request.method == 'GET':
        return render_template('batch-schedule-entry.html')
    else:
        response = batch.schedule_batch(request.form)
        return render_template('batch-schedule-entry.html', response=response)


if __name__ == '__main__':
    db.create()
    app.run(debug=True, port=5001)

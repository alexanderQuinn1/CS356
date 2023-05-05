from flask import Flask, render_template, request
import pika
import json

from maintenance import save_maintenance_activity
from productionSchedule import create_batch

app = Flask(__name__)


@app.route('/')
def run_app():
    return render_template('dashboard.html')


@app.route('/dashboard')
def run_dashboard():
    return render_template('dashboard.html')


@app.route('/productionLine')
def run_productionLine():
    return render_template('productionLine.html')


@app.route('/productionSchedule')
def run_productionSchedule():
    return render_template('productionSchedule.html')


@app.route('/qualityAssurance')
def run_qualityAssurance():
    return render_template('qualityAssurance.html')


@app.route('/maintenanceLog')
def run_maintenanceLog():
    return render_template('maintenanceLog.html')



@app.route('/qualityAssuranceEntry', methods=['GET', 'POST'])
def run_quality_assurance_entry():
    if request.method == 'GET':
        return render_template('qualityAssuranceEntry.html')
    else:
        response = save_quality_assurance(request.form)
        return render_template('qualityAssuranceEntry.html', response=response)


@app.route('/maintenanceEntry', methods=['GET', 'POST'])
def run_maintenance_entry():
    if request.method == 'GET':
        return render_template('maintenanceEntry.html')
    else:
        response = save_maintenance_activity(request.form)
        return render_template('maintenanceEntry.html', response=response)


@app.route('/batchScheduleEntry', methods=['GET', 'POST'])
def run_batch_schedule_entry():
    if request.method == 'GET':
        return render_template('batchScheduleEntry.html')
    else:
        response = create_batch(request.form)
        return render_template('batchScheduleEntry.html', response=response)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

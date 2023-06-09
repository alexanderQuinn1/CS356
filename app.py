from flask import Flask, render_template, request, redirect, url_for
import database_connection as db
import prod_line_monitor_processor as plm
import models.batch as batch
import models.maintenance_operation as maintenance
import models.passage_qa as qa
import models.batch as batch

app = Flask(__name__)


@app.route('/')
def run_app():
    return redirect('/prod-line-monitor/A')


@app.route('/prod-line-monitor/<prod_line>')
def run_production_line(prod_line):
    heading = 'Production Line Monitor'
    return plm.render_prod_activity(heading, prod_line)


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
    heading = 'Enter QA Test Data'
    if request.method == 'GET':
        return render_template('qa-entry.html', heading=heading)
    else:
        response = qa.save_qa(request.form)
        return render_template('qa-entry.html', heading=heading, response=response)


@app.route('/maintenance-entry', methods=['GET', 'POST'])
def run_maintenance_entry():
    if request.method == 'GET':
        return render_template('maintenance-entry.html')
    else:
        response = maintenance.save_maintenance_activity(request.form)
        return render_template('maintenance-entry.html', response=response)


@app.route('/batch-schedule-entry', methods=['GET', 'POST'])
def run_batch_schedule_entry():
    heading = 'schedule a batch'
    if request.method == 'GET':
        return render_template('batch-schedule-entry.html', heading=heading)
    else:
        response = batch.schedule_batch(request.form)
        return render_template('batch-schedule-entry.html', heading=heading, response=response)


@app.route('/update_passage_monitor', methods=['GET', 'POST'])
def run_passage_monitor_entry():
    if request.method == 'GET':
        return render_template('passage-monitor-entry.html', heading='Enter Passage Monitoring Data')


@app.route('/move_to_next_stage/<prod_line>/<batch_no>/<current_stage_id>')
def move_batch_to_next_stage(prod_line, batch_no, current_stage_id):
    plm.update_batch_stage(batch_no, current_stage_id)
    return redirect('/prod-line-monitor/{line}'.format(line=prod_line))


if __name__ == '__main__':
    # db.create()
    app.run(debug=True, port=5001)

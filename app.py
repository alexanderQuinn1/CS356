from flask import Flask, render_template, request, redirect
import database_connection as db
import prod_line_monitor_processor as plm
import fill_room_processor as frm
import models.maintenance_operation as maintenance
import models.passage_qa as qa
import models.batch as batch
import models.passage_monitor as passage_monitor
import models.flask_monitor as flask_monitor

app = Flask(__name__)

# Main Navigation #
@app.route('/')
def run_app():
    return redirect('/prod-line-monitor/A')


@app.route('/prod-line-monitor/<tab>')
def run_production_line(tab):
    heading = 'Production Line Monitor'
    if tab == 'fill-room':
        return frm.render_fill_room(heading, tab)
    else:
        return plm.render_prod_activity(heading, tab)


@app.route('/prod-schedule')
def run_production_schedule():
    heading = 'Production Schedule'
    return plm.render_prod_schedule_calender(heading)


@app.route('/qa-log')
def run_quality_assurance():
    return render_template('qa-log.html', heading="Quality Assurance Log")


@app.route('/maintenance-log')
def run_maintenance_log():
    return render_template('maintenance-log.html', heading="Maintenance Log")


# Data Entry End-Points #
@app.route('/passage-qa-entry', methods=['GET', 'POST'])
def render_passage_qa_entry_screen():
    heading = 'Passage QA Entry'
    if request.method == 'GET':
        return render_template('passage-qa-entry.html', heading=heading)
    else:
        # TODO response = passage_qa.add(request.form)
        return render_template('passageqa-entry.html', heading=heading)


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


@app.route('/update_passage_monitor/<prod_line>/<batch_no>/<monitor_id>', methods=['GET', 'POST'])
def run_passage_monitor_entry(prod_line, batch_no, monitor_id):
    if request.method == 'GET':
        return render_template('passage-monitor-entry.html', heading='Enter Passage Monitoring Data', prod_line=prod_line, batch_no=batch_no, monitor_id=monitor_id)
    if request.method == 'POST':
        validation = passage_monitor.update(monitor_id, request.form['peristaltic_pump'], request.form['cell_count'])
        if validation is not None:
            return render_template('passage-monitor-entry.html', heading='Enter Passage Monitoring Data', prod_line=prod_line, batch_no=batch_no, monitor_id=monitor_id, form_validation=validation)
        else:
            return redirect('/prod-line-monitor/{line}'.format(line=prod_line))


@app.route('/maintenance-batch-entry', methods=['GET', 'POST'])
def run_main_batch_entry():
    heading = 'schedule a batch'
    if request.method == 'GET':
        return render_template('maintenance-batch-entry.html', heading=heading)
    else:
        response = batch.schedule_batch(request.form)
        return render_template('maintenance-batch-entry.html', heading=heading, response=response)


@app.route('/maintenance-batch-entry/<entry_type>/', methods=['GET', 'POST'])
def run_main_entry(entry_type):
    heading = 'Add to Schedule'
    return plm.render_batch_monitor_entry(heading, entry_type)


@app.route('/update_expansion_monitor/<prod_line>/<batch_no>/<flask_monitor_id>', methods=['GET', 'POST'])
def run_expansion_monitor_entry(prod_line, batch_no, flask_monitor_id):
    if request.method == 'GET':
        return render_template('expansion-monitor-entry.html', heading='Enter Flask Monitoring Data', prod_line=prod_line, batch_no=batch_no, monitor_id=flask_monitor_id)
    if request.method == 'POST':
        validation = flask_monitor.update(flask_monitor_id, request.form['temperature'], request.form['ph'], request.form['osmolality'])
        if validation is not None:
            return render_template('expansion-monitor-entry.html', heading='Enter Flask Monitoring Data', prod_line=prod_line, batch_no=batch_no, monitor_id=flask_monitor_id, form_validation=validation)
        else:
            return redirect('/prod-line-monitor/{line}'.format(line=prod_line))


@app.route('/move_to_next_stage/<prod_line>/<batch_no>/<current_stage_id>')
def move_batch_to_next_stage(prod_line, batch_no, current_stage_id):
    plm.update_batch_stage(batch_no, current_stage_id)
    return redirect('/prod-line-monitor/{line}'.format(line=prod_line))


@app.route('/maintenance-details/<maintenance_id>')
def run_maintenance_details(maintenance_id):
    heading = 'Maintenance Operation Details'
    return render_template('maintenance-operation-details.html', heading=heading)


if __name__ == '__main__':
    db.create()
    app.run(debug=True, port=5001)

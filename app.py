from flask import Flask, render_template, request, redirect
import database_connection as db
import controllers.production_monitor as production_monitor_controller
import controllers.passage as passage_controller
import controllers.expansion as expansion_controller
import controllers.prod_schedule as prod_schedule_controller
import processors.batch as batch_processor

app = Flask(__name__)

# Main Navigation #
@app.route('/')
def run_app():
    return redirect('/production-monitoring/A')


@app.route('/production-monitoring/<production_facility>')
def run_production_line(production_facility):
    return production_monitor_controller.render_activity('Production Monitoring', production_facility)


@app.route('/prod-schedule')
def run_production_schedule():
    return render_template('production-schedule/production-schedule.html', heading="Production Schedule")


@app.route('/qa-log')
def run_quality_assurance():
    return render_template('qa-log/qa-log.html', heading="Quality Assurance Log")


@app.route('/maintenance-log')
def run_maintenance_log():
    return render_template('maintenance-log/maintenance-log.html', heading="Maintenance Log")


# Data Entry End-Points #
@app.route('/add-passage-qa/<prod_line>/<batch_no>/', methods=['GET', 'POST'])
def run_add_passage_qa(prod_line, batch_no):
    return passage_controller.render_add_qa(request, prod_line, batch_no)


@app.route('/update_passage_monitor/<prod_line>/<batch_no>', methods=['GET', 'POST'])
def run_update_passage_monitor(prod_line, batch_no):
    return passage_controller.render_update_monitor(request, prod_line, batch_no)


# @app.route('/maintenance-batch-entry/<entry_type>/', methods=['GET', 'POST'])
# def run_main_entry(entry_type):
#     heading = 'Add to Schedule'
#     return prod_schedule_controller.render_add_prod_activity(heading)
#

@app.route('/update_expansion_monitor/<prod_line>/<batch_no>/<flask_monitor_id>', methods=['GET', 'POST'])
def run_update_expansion_monitor(prod_line, batch_no, flask_monitor_id):
    return expansion_controller.render_update_expansion_monitor(request, prod_line, batch_no, flask_monitor_id)


@app.route('/move_batch_next_stage/<prod_line>/<batch_no>')
def run_move_batch_next_stage(prod_line, batch_no):
    batch_processor.update_stage(batch_no)
    return redirect('/production-monitoring/{line}'.format(line=prod_line))


@app.route('/maintenance-activity-details/<maintenance_id>')
def run_maintenance_activity_details(maintenance_id):
    return render_template('maintenance-operation-details.html', heading='Maintenance Activity Details')


@app.route('/add-prod-activity', methods=['GET', 'POST'])
def run_add_prod_activity():
    return prod_schedule_controller.render_add_prod_activity(request)


if __name__ == '__main__':
    db.create()
    app.run(debug=True, port=5001)

from flask import Flask, render_template, request, redirect
import database_connection as db
import controllers.production_monitor as production_monitor_controller
import controllers.passage as passage_controller
import controllers.expansion as expansion_controller
import controllers.prod_schedule as prod_schedule_controller
import controllers.fill_room as fill_room_controller
import processors.batch as batch_processor

app = Flask(__name__)


# Error Page Function #
def render_error_page(error):
    error_message = str(error)
    return render_template('error.html', error_message=error_message)


# Main Navigation #
@app.route('/')
def run_app():
    try:
        return redirect('/production-monitoring/A')
    except Exception as e:
        return render_error_page(e)


@app.route('/production-monitoring/<production_facility>')
def run_production_line(production_facility):
    try:
        return production_monitor_controller.render_activity('Production Monitoring', production_facility)
    except Exception as e:
        return render_error_page(e)


@app.route('/prod-schedule')
def run_production_schedule():
    try:
        return prod_schedule_controller.render_activity('Production Schedule')
    except Exception as e:
        return render_error_page(e)


@app.route('/qa-log')
def run_quality_assurance():
    try:
        return render_template('qa-log/qa-log.html', heading="Quality Assurance Log")
    except Exception as e:
        return render_error_page(e)


@app.route('/maintenance-log')
def run_maintenance_log():
    try:
        return render_template('maintenance-log/maintenance-log.html', heading="Maintenance Log")
    except Exception as e:
        return render_error_page(e)


# Data Entry End-Points #
@app.route('/add-passage-qa/<prod_line>/<batch_no>/', methods=['GET', 'POST'])
def run_add_passage_qa(prod_line, batch_no):
    try:
        return passage_controller.render_add_qa(request, prod_line, batch_no)
    except Exception as e:
        return render_error_page(e)


@app.route('/update_passage_monitor/<prod_line>/<batch_no>', methods=['GET', 'POST'])
def run_update_passage_monitor(prod_line, batch_no):
    try:
        return passage_controller.render_update_monitor(request, prod_line, batch_no)
    except Exception as e:
        return render_error_page(e)


@app.route('/update_expansion_monitor/<prod_line>/<batch_no>/<flask_monitor_id>', methods=['GET', 'POST'])
def run_update_expansion_monitor(prod_line, batch_no, flask_monitor_id):
    try:
        return expansion_controller.render_update_expansion_monitor(request, prod_line, batch_no, flask_monitor_id)
    except Exception as e:
        return render_error_page(e)


@app.route('/move_batch_next_stage/<prod_line>/<batch_no>')
def run_move_batch_next_stage(prod_line, batch_no):
    try:
        batch_processor.update_stage(batch_no)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))
    except Exception as e:
        return render_error_page(e)


@app.route('/add-fill-room-qa/<prod_line>/<batch_no>/', methods=['GET', 'POST'])
def run_add_fill_room_qa(prod_line, batch_no):
    try:
        return fill_room_controller.render_add_qa(request, prod_line, batch_no)
    except Exception as e:
        return render_error_page(e)


@app.route('/update-fill-room-monitor/<prod_line>/<batch_no>/', methods=['GET', 'POST'])
def run_update_fill_room_monitor(prod_line, batch_no):
    try:
        return fill_room_controller.render_update_monitor(request, prod_line, batch_no)
    except Exception as e:
        return render_error_page(e)


@app.route('/maintenance-activity-details/<maintenance_id>')
def run_maintenance_activity_details(maintenance_id):
    try:
        return render_template('maintenance-log/maintenance-activity-details.html',
                               heading='Maintenance Activity Details')
    except Exception as e:
        return render_error_page(e)


@app.route('/add-prod-activity', methods=['GET', 'POST'])
def run_add_prod_activity():
    try:
        return prod_schedule_controller.render_add_prod_activity(request)
    except Exception as e:
        return render_error_page(e)


@app.route('/error_mock_page', methods=['GET', 'POST'])
def run_error_mock_page():
    e = 'error.................'
    return render_error_page(e)


try:
    db.create()
    app.run()
except Exception as e:
    print(f"An error occurred: {str(e)}")
    render_error_page(e)

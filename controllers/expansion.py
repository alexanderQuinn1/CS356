from flask import render_template, redirect
import processors.batch as batch_processor
import processors.expansion as expansion_processor
import models.flask_monitor as flask_monitor_repo


UPDATE_EXPANSION_MONITOR_HTML = 'production-monitoring/prod-line-monitor/batch-monitor/expansion/expansion-monitor-entry.html'


def render_update_expansion_monitor(request, prod_line, batch_no, flask_monitor_id):
    heading = 'Update Flask Monitoring Data'
    if request.method == 'GET':
        batch = batch_processor.get_batch(batch_no)
        flask = flask_monitor_repo.get(flask_monitor_id)
        return render_template(UPDATE_EXPANSION_MONITOR_HTML, heading=heading, production_facility=prod_line,
                               batch=batch, flask=flask)
    elif request.method == 'POST':
        expansion_processor.update_flask_monitor(request.form, flask_monitor_id)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))

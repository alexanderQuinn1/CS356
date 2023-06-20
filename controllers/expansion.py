from flask import render_template, request, redirect
import processors.batch as batch_processor
import processors.expansion as expansion_processor

UPDATE_EXPANSION_MONITOR_HTML = 'production-monitoring/prod-line-monitor/batch-monitor/expansion/expansion-monitor-entry.html'


def render_update_expansion_monitor(request, prod_line, batch_no, flask_monitor_id):
    heading = 'Update Flask Monitoring Data'
    if request.method == 'GET':
        batch = batch_processor.get_batch(batch_no)
        return render_template(UPDATE_EXPANSION_MONITOR_HTML, heading=heading, production_facility=prod_line,
                               batch=batch, flask_monitor_id=flask_monitor_id)
    if request.method == 'POST':
        form_validation = expansion_processor.update_flask_monitor(request.form, flask_monitor_id)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))

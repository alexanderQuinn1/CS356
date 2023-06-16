
def render_update_expansion_monitor(heading, request, prod_line, batch, flask_monitor_id):
    heading = 'Update Flask Monitoring Data'
    batch = {}
    if request.method == 'GET':
        return render_template('expansion-monitor-entry.html', heading=heading, prod_line=prod_line, batch=batch,
                               flask_monitor_id=flask_monitor_id)
    if request.method == 'POST':
        validation = flask_monitor.update(flask_monitor_id, request.form['temperature'], request.form['ph'],
                                          request.form['osmolality'])
        if validation is not None:
            return render_template('expansion-monitor-entry.html', heading='Enter Flask Monitoring Data',
                                   prod_line=prod_line, batch=batch, monitor_id=flask_monitor_id,
                                   form_validation=validation)
        else:
            return redirect('/production-monitoring/{line}'.format(line=prod_line))

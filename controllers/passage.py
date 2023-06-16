import models.passage_qa as passage_qa_repo


def render_add_qa(heading, request, prod_line, batch):
    heading = 'Add Passage QA Data'
    batch = {}
    if request.method == 'GET':
        return render_template('passage-qa-entry.html', heading=heading)
    elif request.method == 'POST':
        form_validation = passage_qa_repo.insert(passage_id, request.form)
        if form_validation is not None:
            return render_template('passage-qa-entry.html', heading=heading, form_validation=form_validation)
        else:
            return redirect('/production-monitoring/{line}'.format(line=prod_line))


def render_update_monitor(heading, request, prod_line, batch):
    heading = 'Update Passage Monitoring Data'
    batch = {}
    if request.method == 'GET':
        return render_template('passage-monitor-entry.html', heading=heading, prod_line=prod_line, batch=batch)
    if request.method == 'POST':
        form_validation = passage_monitor.update(monitor_id, request.form['peristaltic_pump'], request.form['cell_count'])
        if validation is not None:
            return render_template('production-monitoring.html', heading='Enter Passage Monitoring Data',
                                   prod_line=prod_line, batch_no=batch_no, monitor_id=monitor_id,
                                   form_validation=validation)
        else:
            return redirect('/production-monitoring/{line}'.format(line=prod_line))

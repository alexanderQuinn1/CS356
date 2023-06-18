from flask import render_template, request, redirect
import processors.batch as batch_processor
import processors.passage as passage_processor

ADD_PASSAGE_QA_HTML = 'production-monitoring/prod-line-monitor/batch-monitor/passage/passage-qa-entry.html'
UPDATE_PASSAGE_MONITOR_HTML = 'production-monitoring/prod-line-monitor/batch-monitor/passage/passage-monitor-entry.html'


def render_add_qa(request, prod_line, batch_no):
    heading = 'Add Passage QA Data'
    batch = batch_processor.get_batch(batch_no)
    if request.method == 'GET':
        return render_template(ADD_PASSAGE_QA_HTML, heading=heading, production_facility=prod_line, batch=batch)
    elif request.method == 'POST':
        passage_processor.add_qa(request.form, batch)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))


def render_update_monitor(request, prod_line, batch_no):
    heading = 'Update Passage Monitoring Data'
    batch = batch_processor.get_batch(batch_no)
    if request.method == 'GET':
        return render_template(UPDATE_PASSAGE_MONITOR_HTML, heading=heading, production_facility=prod_line, batch=batch)
    if request.method == 'POST':
        form_validation = passage_processor.update_monitor(request.form, batch)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))

from flask import render_template, redirect
import processors.batch as batch_processor
import processors.fill_room as fill_room_processor

ADD_FILL_ROOM_QA_HTML = 'production-monitoring/fill-room/fill-room-qa-entry.html'
UPDATE_FILL_ROOM_MONITOR_HTML = 'production-monitoring/fill-room/fill-room-monitor-entry.html'


def render_add_qa(request, prod_line, batch_no):
    heading = 'Add Fill Room QA Data'
    batch = batch_processor.get_batch(batch_no)
    if request.method == 'GET':
        return render_template(ADD_FILL_ROOM_QA_HTML, heading=heading, production_facility=prod_line, batch=batch)
    elif request.method == 'POST':
        fill_room_processor.add_qa(request.form, batch)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))


def render_update_monitor(request, prod_line, batch_no):
    heading = 'Update Fill Room Monitoring Data'
    batch = batch_processor.get_batch(batch_no)
    if request.method == 'GET':
        return render_template(UPDATE_FILL_ROOM_MONITOR_HTML, heading=heading, production_facility=prod_line, batch=batch)
    if request.method == 'POST':
        fill_room_processor.update_monitor(request.form, batch)
        return redirect('/production-monitoring/{line}'.format(line=prod_line))

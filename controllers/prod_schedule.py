from flask import render_template, request, redirect

ADD_PROD_ACTIVITY_HTML = 'production-schedule/prod-activity-entry.html'


def render_add_prod_activity(request):
    heading = 'Schedule a Production Activity'
    if request.method == 'GET':
        return render_template(ADD_PROD_ACTIVITY_HTML, heading=heading)
    else:
        form_validation = batch.schedule_batch(request.form)
        if form_validation is not None:
            return render_template(ADD_PROD_ACTIVITY_HTML, heading=heading, form_validation=form_validation)
        else:
            return redirect('/production-schedule')


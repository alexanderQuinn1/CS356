from flask import render_template, redirect
import processors.prod_sched as prod_sched_processor

ADD_PROD_ACTIVITY_HTML = 'production-schedule/prod-activity-entry.html'

PROD_SCHEDULE_HTML = 'production-schedule/production-schedule.html'


def render_add_prod_activity(request):
    heading = 'Schedule a Production Activity'
    if request.method == 'GET':
        return render_template(ADD_PROD_ACTIVITY_HTML, heading=heading)
    else:
        form_validation = prod_sched_processor.schedule_activity(request.form)
        if form_validation is not None:
            return render_template(ADD_PROD_ACTIVITY_HTML, heading=heading, form_validation=form_validation)
        else:
            return redirect('/prod-schedule')


def render_activity(heading):
    events = prod_sched_processor.formatted_events()
    return render_template(PROD_SCHEDULE_HTML, heading=heading, sched_events=events)

import models.prod_schedule as prod_sched
from flask import render_template

def render_prod_schedule_calender(heading):
    return render_template('prod-line-schedule.html', heading=heading, prod_line=tab)

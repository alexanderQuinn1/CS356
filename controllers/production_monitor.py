from flask import render_template
import models.prod_schedule as prod_schedule_repo
import processors.batch as batch_processor
import processors.prod_stage as prod_stage_processor
import processors.fill_room as fill_room_processor


BATCH_MONITOR_HTML = 'production-monitoring/prod-line-monitor/batch-monitor/batch-monitor.html'
FILL_ROOM_MONITOR_HTML = 'production-monitoring/fill-room/fill-room-monitor.html'
MAINTENANCE_HTML = 'production-monitoring/prod-line-monitor/prod-line-maintenance.html'
IDLE_HTML = 'production-monitoring/prod-line-monitor/prod-line-idle.html'


def render_activity(heading, production_facility):
    if production_facility == 'fill-room':
        batches = fill_room_processor.get_batches_in_fillroom()
        return render_template(FILL_ROOM_MONITOR_HTML, heading=heading, production_facility=production_facility, batches=batches)
    prod_activity = prod_schedule_repo.get_by_prod_line(production_facility)
    if prod_activity is None:
        return render_template(IDLE_HTML, heading=heading, production_facility=production_facility)
    elif prod_activity['activity_type'] == 'batch':
        return render_batch_manufacture(heading, production_facility, prod_activity)
    elif prod_activity['activity_type'] == 'maintenance':
        return render_maintenance(heading, production_facility, prod_activity)


def render_batch_manufacture(heading, prod_line, prod_activity):
    batch = batch_processor.get_batch_by_prod_schedule(prod_activity['id'])
    stages = prod_stage_processor.get_monitoring_stages(batch)
    return render_template(BATCH_MONITOR_HTML, heading=heading, production_facility=prod_line, stages=stages, batch=batch)


def render_maintenance(heading, prod_line, prod_activity):
    return render_template(MAINTENANCE_HTML, heading=heading, production_facility=prod_line)
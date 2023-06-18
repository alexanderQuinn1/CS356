from flask import render_template, request, redirect
import models.prod_schedule as prod_schedule_repo
import models.maintenance_operation as maintenance_operation_repo
import processors.batch as batch_processor
import processors.prod_stage as prod_stage_processor

BATCH_MONITOR_HTML = 'production-monitoring/prod-line-monitor/batch-monitor/batch-monitor.html'
MAINTENANCE_HTML = 'production-monitoring/prod-line-monitor/prod-line-maintenance.html'
IDLE_HTML = 'production-monitoring/prod-line-monitor/prod-line-idle.html'


def render_activity(heading, production_facility):
    if production_facility == 'fill room':
        # TODO
        return None
    prod_activity = prod_schedule_repo.get_by_prod_line(production_facility)
    if prod_activity is None:
        return render_template(IDLE_HTML, heading=heading, production_facility=production_facility)
    elif prod_activity['type'] == 'batch_manufacture':
        return render_batch_manufacture(heading, production_facility, prod_activity)
    elif prod_activity['type'] == 'maintenance':
        return render_maintenance(heading, production_facility, prod_activity)


def render_batch_manufacture(heading, prod_line, prod_activity):
    batch = batch_processor.get_batch_by_prod_schedule(prod_activity['id'])
    stages = prod_stage_processor.get_display_stages(batch['active_stage']['id'])
    return render_template(BATCH_MONITOR_HTML, heading=heading, production_facility=prod_line, stages=stages, batch=batch)


def render_maintenance(heading, prod_line, prod_activity):
    maintenance = maintenance_operation_repo.get_maintenance_activity(prod_activity['id'])
    return render_template(MAINTENANCE_HTML, heading=heading, production_facility=prod_line, maintenance=maintenance)
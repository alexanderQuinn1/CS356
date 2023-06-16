from flask import render_template
import models.prod_schedule as prod_schedule_repo
import models.prod_stage_lookup as prod_stage_lookup_repo
import models.maintenance_operation as maintenance_operation_repo
import processors.batch as batch_processor


def render_activity(heading, production_facility):
    if production_facility == 'fill room':
        # TODO
        return None
    prod_activity = prod_schedule_repo.get_by_prod_line(production_facility)
    if prod_activity is None:
        return render_template('prod-line-idle.html', heading=heading, prod_line=production_facility)
    elif prod_activity['type'] == 'batch_manufacture':
        return render_batch_manufacture(heading, production_facility, prod_activity)
    elif prod_activity['type'] == 'maintenance':
        return render_maintenance(heading, production_facility, prod_activity)


def render_batch_manufacture(heading, prod_line, prod_activity):
    b = batch_processor.get_batch_by_prod_schedule(prod_activity['id'])
    stages = prod_stage_lookup_repo.get_all_stages_based_on_step(b['current_stage'])
    stage_type = prod_stage_lookup_repo.get_stage_type(b['current_stage'])

    if stage_type == 'expansion':
        return render_template('prod-line-batch-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=b)
    elif stage_type == 'passage':
        return render_template('prod-line-batch-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=b)
    else:
        return render_template('prod-line-batch-monitor.html', heading=heading, prod_line=prod_line, stages=stages,
                               batch=b)


def render_maintenance(heading, prod_line, prod_activity):
    maintenance = maintenance_operation_repo.get_maintenance_activity(prod_activity['id'])
    return render_template('prod-line-maintenance.html', heading=heading, prod_line=prod_line, maintenance=maintenance)
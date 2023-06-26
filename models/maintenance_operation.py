import database_connection as db


def insert(plant_id, description, man_hours, parts_replaced, cost, shutdown_required, planned_activity, prod_schedule_id):
    # TODO
    query = """INSERT INTO `miracle_cure_biotech`.`maintenance_operation`
    (
    `plant_id`,
    `description`,
    `man_hours`,
    `parts_replaced`,
    `cost`,
    `shutdown_required`,
    `planned_activity`,
    `prod_schedule_id`)
    VALUES
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s;
    """
    last_id = db.insert_commit(query, (plant_id, description, man_hours, parts_replaced, cost, shutdown_required, planned_activity, prod_schedule_id))
    return last_id


def get_by_prod_schedule(prod_schedule_id):
    return {
        'id': 2,
        'description': 'replacement of peristaltic pump'
    }


def get_by_id(maintenance_id):
    # TODO
    return

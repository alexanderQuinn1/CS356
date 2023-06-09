import database_connection
import mysql.connector


def get_cursor():
    database_name = "miracle_cure_biotech"
    return database_connection.connect_database(database_name).cursor()


# Get the current production line status
def prodScheduleCurrent():
    cursor = get_cursor()
    prod_schedule_query = """
    SELECT prod_schedule_id , prod_line, activity_type 
    FROM miracle_cure_biotech.production_schedule
    WHERE start < now() AND end > NOW();    
    """
    cursor.execute(prod_schedule_query)
    production_schedule = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()

    return production_schedule


def production_schedule_passage():
    cursor = get_cursor()
    prod_schedule_query = """SELECT batch.batch_no , stage_lookup.stage_name, production_schedule.prod_line 
    FROM batch
    join production_schedule on batch.prod_schedule_id = production_schedule.prod_schedule_id 
    join stage_lookup on batch.current_stage = stage_lookup.stage_id
    where production_schedule.start < now() AND production_schedule.end > NOW() AND production_schedule.activity_type = "batch";
    """

    cursor.execute(prod_schedule_query)
    currentbatches = cursor.fetchall()
    currentbatches_in_passage = []
    currentbatches_in_expansion = []
    currentbatches_in_fill_room = []

    for currentbatch in currentbatches:
        batch_no, stage_name, prod_line = currentbatch

        if "passage" in stage_name:
            passage_query = """SELECT passage.passage_id, batch.batch_no, stage_lookup.stage_name, passage_monitor.peristaltic_pump , passage_monitor.cell_count , phase_qa.passed
            FROM passage_monitor 
            JOIN passage  ON passage_monitor.passage_monitor_id = passage.passage_id
            JOIN batch  ON passage.batch_id = batch.batch_no
            JOIN phase_qa  ON passage.passage_id = phase_qa.passage_id
            JOIN stage_lookup  ON passage.stage = stage_lookup.stage_id
            WHERE stage_lookup.stage_name = %s
            AND batch.batch_no = %s
            """
            cursor.execute(passage_query, (stage_name, batch_no))
            batches_passage = cursor.fetchall()
            for batch in batches_passage:
                expansion = {
                    'passage_id': batch[0],
                    'batch_no': batch[1],
                    'stage_name': batch[2],
                    'peristaltic_pump': batch[3],
                    'cell_count': batch[4],
                    'passed': batch[5]
                }

                currentbatches_in_passage.append(expansion)
            print(currentbatches_in_passage)

        if "expansion" in stage_name:

            expansion_query = """select
            batch.batch_no,
            production_schedule.prod_line,
            product_type.min_temp, flask_monitor.temp, product_type.max_temp, 
            product_type.min_ph ,flask_monitor.ph, product_type.max_ph, 
            product_type.min_osmoality,flask_monitor.osmoality, product_type.max_osmoality
            from flask_monitor
            join expansion on flask_monitor.expansion_id = expansion.expansion_id
            join batch on expansion.batch_id = batch.batch_no
            join stage_lookup on expansion.stage = stage_lookup.stage_id
            join product_type on batch.prod_type_code = product_type.prod_type_code
            join production_schedule on batch.prod_schedule_id = production_schedule.prod_schedule_id
            where stage_lookup.stage_name = %s and batch_id = %s
            """
            cursor.execute(expansion_query, (stage_name, batch_no))
            batches_expansion = cursor.fetchall()
            for batch in batches_expansion:
                expansion = {
                    'batch_no': batch[0],
                    'prod_line': batch[1],
                    'min_temp': batch[2],
                    'temp': batch[3],
                    'max_temp': batch[4],
                    'min_ph': batch[5],
                    'ph': batch[6],
                    'max_ph': batch[7],
                    'min_osmoality': batch[8],
                    'osmoality': batch[9],
                    'max_osmoality': batch[10]

                }
                currentbatches_in_expansion.append(expansion)
            print(currentbatches_in_expansion)

        if "fill room" in stage_name:
            fill_room_query = """select batch.batch_no,fill_room_monitor.temp,fill_room_monitor.humidity, fill_room_monitor.last_stir_delta , 
            fill_room_qa.mycoplasma, fill_room_qa.virus_testing, fill_room_qa.amino_acids, fill_room_qa.trace_elements
            from fill_room_monitor
            join fill_room on fill_room_monitor.fill_room_id = fill_room.fill_room_id
            join batch on fill_room.batch_id = batch.batch_no
            join stage_lookup on fill_room.stage = stage_lookup.stage_id
            join fill_room_qa on fill_room.fill_room_id = fill_room_qa.fill_room_id
            where stage_lookup.stage_name = %s and batch.batch_no = %s
            """
            cursor.execute(fill_room_query, (stage_name, batch_no))
            batches_fill = cursor.fetchall()
            for batch in batches_fill:
                fill_room = {
                    'batch_no': batch[0],
                    'temp': batch[1],
                    'humidity': batch[2],
                    'last_stir_delta': batch[3],
                    'mycoplasma': batch[4],
                    'virus_testing': batch[5],
                    'amino_acids': batch[6],
                    'trace_elements': batch[7]

                }
                currentbatches_in_fill_room.append(fill_room)
            print(currentbatches_in_fill_room)


def production_schedule_maintenance():
    cursor = get_cursor()
    prod_schedule_maintenance = """SELECT maintenance_operation.*
    FROM maintenance_operation
    join production_schedule on maintenance_operation.prod_schedule_id = production_schedule.prod_schedule_id 
    where production_schedule.start < now() AND production_schedule.end > NOW() AND production_schedule.activity_type = "maintenance";
    """
    cursor.execute(prod_schedule_maintenance)

    print(cursor.fetchall())


production_schedule_passage()


def get_batch_stage(batch):
    cursor = get_cursor()
    prod_batch = """SELECT current_stage from miracle_cure_biotech.Batch Where batch_no = "IRV2305001";"""
    cursor.execute(prod_batch)
    print(cursor.fetchall())


def update_batch_stage(batch, stage):
    cursor = get_cursor()
    prod_batch = """SELECT current_stage from miracle_cure_biotech.Batch Where batch_no = "IRV2305001";"""
    cursor.execute(prod_batch)
    print(cursor.fetchall())

def schedule_batch(form):
    print(form)
    # validate prod line doesnt have another batch scheduled simultaneously
    # prod_end = start_time + prod_duration
    # batch_no = IRVyymm9999
    return 'batch IRVyymm9999 scheduled'


def get_batch_in_production(prod_schedule_id):
    return {
        'batch_no': 'IRV99999999',
        'prod_type': 'XXXX99',
        'current_stage': 3,
    }
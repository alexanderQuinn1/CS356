import models.batch as batch_repo
import models.fill_room_qa as fill_room_qa_repo
import processors.batch as batch_processor


def get_batches_in_fillroom():
    batch_numbers = batch_repo.get_in_fill_room()
    batches = []
    for batch_no in batch_numbers:
        batches.append(batch_processor.get_batch(batch_no))
    return batches


def get_qa(batch_no):
    qa = fill_room_qa_repo.get(batch_no)
    if not qa:
        return None

    qa['result'] = 'passed' if qa['passed'] else 'failed'
    qa['colour'] = 'green' if qa['passed'] else 'red'
    return qa

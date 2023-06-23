import database_connection as db
import models.fill_room_monitor as fill_room_repo
# func to get all batches where stage is fillroom (get from controller)
# for each get batch


def get_batches_in_fillroom():
    batch_numbers = batch_repo.get_in_fill_room()
    batches = []
    for batch_no in batch_numbers:
        batches.append(batch_processor.get_batch(batch_no))
    return batches



if __name__ == '__main__':
    print(get_batchs_in_fillroom())

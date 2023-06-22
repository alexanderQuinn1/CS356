import database_connection as db
import models.fill_room_monitor as fill_room_repo
# func to get all batches where stage is fillroom (get from controller)
# for each get batch


def get_batchs_in_fillroom():
    fill_rooms = fill_room_repo.get()
    return fill_rooms


if __name__ == '__main__':
    print(get_batchs_in_fillroom())

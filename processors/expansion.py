import models.flask_monitor as flask_monitor_repo


def update_flask_monitor(form, flask_monitor_id):
    flask_monitor_repo.update(flask_monitor_id, form['temperature'], form['ph'], form['osmolality'])

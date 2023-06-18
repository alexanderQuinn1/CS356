import models.flask_monitor as flask_monitor_repo


def update_flask_monitor(form, flask_monitor_id):
    temperature = int(form['temperature'])
    ph = int(form['ph'])
    osmolality = int(form['osmolality'])

    flask_monitor_repo.update(flask_monitor_id, temperature, ph, osmolality)

import models.passage_qa as passage_qa


def save_qa(passage_id, form):
    passed = __has_passed(form['ph'], form['osmolality'], form['sterility'])
    passage_qa.insert(passage_id, datetime.now(), form['cell_count'], form['ph'], form['osmolality'], form['sterility'], passed)
    return None


def get_qa_results(passage_id):
    return {
        'status': 'passed',
        'colour': 'green'
    }


def __has_passed(ph, osmolality, sterility):
    return True

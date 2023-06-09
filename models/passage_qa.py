def save_qa(form):
    print(form)
    return 'Quality Assurance Saved'


def get_qa_outcome(passage_id):
    return {
        'status': 'pass',
        'colour': 'green'
    }


def add_qa_details(qa):
    if not qa:
        return None
    print(qa)
    qa['result'] = 'passed' if qa['passed'] else 'failed'
    qa['colour'] = 'green' if qa['passed'] else 'red'
    qa['failures'] = analysis_to_list(qa['analysis'])


def analyse_results(product, ph, osmolality, sterility):
    failures = []
    if ph < product['min_ph']:
        failures.append('sample is too acidic, ph must be regulated')
    elif ph > product['max_ph']:
        failures.append('sample is too alkaline, ph must be regulated')
    if osmolality < product['min_osmolality']:
        failures.append('sample is hypotonic, osmolality must be regulated')
    elif osmolality > product['max_osmolality']:
        failures.append('sample is hypertonic, osmolality must be regulated')
    if sterility < product['min_sterility']:
        failures.append('sample is not sterile enough: batch should be disposed')

    return failures


def has_passed(failures):
    return len(failures) == 0


def analysis_to_list(analysis):
    if analysis is None:
        return None
    return analysis.split("|")


def analysis_to_string(analysis):
    if analysis is None or analysis is []:
        return ''
    return '|'.join(analysis)



def analyse_results(product, ph, osmolality, sterility, mycoplasma, virus_testing, amino_acids, trace_elements):
    failures = []
    if ph < product['min_ph']:
        failures.append('sample is too acidic, ph must be regulated')
    elif ph > product['max_ph']:
        failures.append('sample is too alkaline, ph must be regulated')
    elif osmolality < product['min_osmolality']:
        failures.append('sample is hypotonic, osmolality must be regulated')
    elif osmolality > product['max_osmolality']:
        failures.append('sample is hypertonic, osmolality must be regulated')
    elif sterility < product['min_sterility']:
        failures.append('sample is not sterile enough: batch should be disposed')

    return failures


def has_passed(failures):
    return len(failures) == 0

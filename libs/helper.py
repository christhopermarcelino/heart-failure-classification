import pandas as pd

def convert_dictionary_to_dataframe(data):
    dict = {}

    for key, value in data.items():
        dict[key] = [value]

    return pd.DataFrame(dict)

def response_message(result):
    if result == 1:
        return 'Positive'
    return 'Negative'
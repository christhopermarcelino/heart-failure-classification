def data_type_casting(data):
    convert_columns = {
        'age': 'int64',
        'restingbp': 'int64',
        'cholesterol': 'int64',
        'fastingbs': 'int64',
        'maxhr': 'int64',
        'oldpeak': 'float64',
    }

    data = data.astype(convert_columns)

    return data
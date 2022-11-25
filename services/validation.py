def validate(req):
    column = ['age','sex','chestpaintype','restingbp','cholesterol','fastingbs','restingecg','maxhr','exerciseangina','oldpeak','st_slope']
   
    
    for col in column:
        if req[col] == '' or req[col] == None:
            return False

    if int(req['maxhr']) < 60 or int(req['maxhr']) > 202:
        return False

    return True
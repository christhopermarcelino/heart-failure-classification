from flask import Flask, render_template, request, redirect, url_for
import joblib
from os.path import join, dirname, realpath

from libs.helper import convert_dictionary_to_dataframe, response_message
from services.feature_engineering import feature_engineering
from services.data_preprocessing import data_type_casting
from services.validation import validate

app = Flask(__name__)

app.static_folder = 'static'

MODEL_PATH = join(dirname(realpath(__file__)), 'models/model.pkl')
loaded_model = joblib.load(MODEL_PATH)

@app.route("/")
def root():
    return render_template("index.html")
    
@app.route("/predict", methods=['POST'])
def predict():
    message = ''

    if request.method == 'POST':
        req = request.form

        if not validate(req):
            message = 'Invalid'
        else:
            df = convert_dictionary_to_dataframe(req)

            df = data_type_casting(df)

            df = feature_engineering(df)

            [prediction] = loaded_model.predict(df)
            
            message = response_message(prediction)
    else:
        message = 'Error occured. Please try again.'

    data = {
        'req': request.form,
        'message': message
    }

    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
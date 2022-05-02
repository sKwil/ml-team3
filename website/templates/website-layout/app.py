from flask import Flask, escape, request, render_template
import pandas as pd
import joblib



def preprocessDataAndPredict(month, prcp_days_tRay, temp_max_normalRay, temp_min_normalRay, snow_daysRay, cloudsRay):
    # keep all inputs in array
    data = [month, prcp_days_tRay, temp_max_normalRay, temp_min_normalRay, snow_daysRay, cloudsRay]

    # Create Data Frame
    data = pd.DataFrame({'Month': [month],
                         'Freq. of Rain': [prcp_days_tRay],
                        'temp_max_normalRay': [temp_max_normalRay],
                         'temp_min_normalRay': [temp_min_normalRay],
                         'Snow_days': [snow_daysRay],
                         'Cloudy_days': [cloudsRay]
                         })

    # open file for data
    file = open("finalModel.pkl", "rb")

    # Connection both the py data and form data from user to output predictions
    @app.route('/predict', methods=['GET', 'POST'])
    def predict():
        if request.method == "POST":
            # get form data
            month = request.form.get('month')
            prcp_days_tRay = request.form.get('prcp_days_tRay')
            temp_max_normalRay = request.form.get('temp_max_normalRay')
            temp_min_normalRay = request.form.get('temp_min_normalRay')
            snow_daysRay = request.form.get('snow_daysRay')
            cloudsRay = request.form.get('cloudsRay')

            # call preprocessDataAndPredict and pass inputs
            try:
                prediction = preprocessDataAndPredict(month, prcp_days_tRay, temp_max_normalRay, temp_min_normalRay, snow_daysRay, cloudsRay)
                # pass prediction to template
                return render_template('weather.html', prediction=prediction)

            except ValueError:
                return "Please Enter valid values"

            pass
        pass

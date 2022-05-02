from flask import Flask, escape, request, render_template
import pandas as pd
import joblib



def preprocessDataAndPredict(month, prcp_days_tRay, curr_occ, occ_24, occ_week, occ_month):
    # keep all inputs in array
    data = [month, prcp_days_tRay, curr_occ, occ_24, occ_week, occ_month]

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
            curr_day = request.form.get('curr_day')
            curr_time = request.form.get('curr_time')
            curr_occ = request.form.get('curr_occ')
            occ_24 = request.form.get('occ_24')
            occ_week = request.form.get('occ_week')
            occ_month = request.form.get('occ_month')

            # call preprocessDataAndPredict and pass inputs
            try:
                prediction = preprocessDataAndPredict(curr_day, curr_time, curr_occ, occ_24, occ_week, occ_month)
                # pass prediction to template
                return render_template('weather.html', prediction=prediction)

            except ValueError:
                return "Please Enter valid values"

            pass
        pass

from flask import Flask, escape, request, render_template
import pandas as pd
import joblib


def preprocessDataAndPredict(state, curr_time, curr_occ, occ_24, occ_week,
                             occ_month):
    # keep all inputs in array
    data = [curr_day, curr_time, curr_occ, occ_24, occ_week, occ_month]

    # Create Data Frame
    data = pd.DataFrame({'day': [curr_day], 'curr_time': [curr_time],
                         'curr_occ': [curr_occ], 'occ_24': [occ_24],
                         'occ_week': [occ_week],
                         'occ_month': [occ_month]})

    # open file
    file = open("finalModel.pkl", "rb")

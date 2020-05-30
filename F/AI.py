import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64, urllib
from datetime import date
from F.Saeverbank import ElecCostForecast

def AI(store_id,years,months,day):
    _date = date(int(years),int(months),int(day))
    elec_predict,elec_predict_plot=ElecCostForecast(str(_date))
    #plt.plot(range(0, 40))
    days = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    plt.plot(days, elec_predict_plot, marker='o', label='Forecasting')
    plt.savefig('graph.png')
    plt.clf()
    plt.close()
    with open("graph.png", "rb") as R:
        Read=R.read()
    encoded = base64.b64encode(Read)
    #send back
    return elec_predict,encoded
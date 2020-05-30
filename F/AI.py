import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64, urllib

def AI(store_id,years,months,date):
    elec_predict=store_id+years+months+date
    plt.plot(range(0, 40))
    plt.savefig('graph.png')
    with open("graph.png", "rb") as R:
        Read=R.read()
    encoded = base64.b64encode(Read)
    return elec_predict,encoded
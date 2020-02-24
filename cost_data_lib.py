from tkinter import *
from GWE_calculator import gas_data

def save_cost_data():
    entered_gas_cost = gas_data.get()
    entered_water_cost = water_data.get()
    entered_elec_cost = elec_data.get()

    file = open('cost_doc.txt', 'a+')
    file.write (str(entered_gas_cost)+' ')
    file.write (str(entered_water_cost)+' ')
    file.write (str(entered_elec_cost)+' ')
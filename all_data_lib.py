from tkinter import *
import GWE_calculator
def print_all():
    window3 = Toplevel()
    window3.title ("All Data Output")

    printout = StringVar()

    text_area = Label(window3,textvariable = printout, height=400, width=200, bg="white")

    file = open('GWE_data.txt', 'a+')
    lines = file.readlines()
    file.close()

    first_line = lines[0].split()
    last_line = lines[-1].split()
    gas_usage = (float(last_line[1]) - float(first_line[1])) * float(g_cost)
    water_usage = (float(last_line[2]) - float(first_line[2])) * float(w_cost)
    elec_usage = (float(last_line[3]) - float(first_line[3])) * float(e_cost)


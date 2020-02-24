from tkinter import *

def print_yesterday(a):

    def window_close():
        window4.destroy()

    window4 = Toplevel()
    window4.title ("Yesterday's Output")

    printout1 = StringVar()
    printout2 = StringVar()
    printout3 = StringVar()

        # text area1
    text_area1 = Label(window4,textvariable = printout1,bg="white",width=50,anchor=W)
    text_area1.grid (row=0, column=0, padx=1,pady=1)
        # text area2
    text_area2 = Label(window4,textvariable = printout2,bg="white",width=50,anchor=W)
    text_area2.grid (row=1, column=0, padx=1,pady=1)
        # text area3
    text_area3 = Label(window4,textvariable = printout3,bg="white",width=50,anchor=W)
    text_area3.grid (row=2, column=0, padx=1,pady=1)

    # close button
    close_button = Button(window4,text="close", command= window_close)
    close_button.grid (row=3,column=0,stick=E)

    file = open('GWE_data.txt', 'r')
    lines = file.readlines()
    file.close()
    latest_reading = lines[-1]
    previous_reading = lines[-2]
    latest_reading = latest_reading.split()
    previous_reading = previous_reading.split()

    gas_usage = (float(latest_reading[1]) - float(previous_reading[1])) * float(a[0]) 
    water_usage = (float(latest_reading[2]) - float(previous_reading[2])) * float(a[1]) 
    elec_usage = (float(latest_reading[3]) - float(previous_reading[3])) * float(a[2]) 
    
    printout1 = printout1.set('Gas usage for ' + previous_reading[0] + ' was ' + str(round(gas_usage, 2)) + ' euros.')
    printout2 = printout2.set('Water usage for ' + previous_reading[0] + ' was ' + str(round(water_usage, 2)) + ' euros.')
    printout3 = printout3.set('Electricity usage for ' + previous_reading[0] + ' was ' + str(round(elec_usage, 2)) + ' euros.')
from tkinter import *

def add_data_win():

    # define functions
    def window_close():
        window2.destroy()

    def save_data():
        print("data saved")
        # get your strings out
        entered_date = usage_date_data.get()
        entered_gas = entry_gas_data.get()
        entered_water = entry_water_data.get()
        entered_elec = entry_elec_data.get()
        print(entered_date)

        # then save said strings in a file
        file = open('GWE_data.txt', 'a+')
        file.write (str(entered_date)+' ')
        file.write (str(entered_gas)+' ')
        file.write (str(entered_water)+' ')
        file.write (str(entered_elec)+'\n')
        file.close()

    window2 = Toplevel()
    window2.title ("Add Usage Data")

    # define labels
    label_date = Label(window2,text="Date")
    label_gas = Label(window2,text="Gas")
    label_water = Label(window2,text="Water")
    label_elec = Label(window2,text="Elec")

    # define variables
    usage_date_data = StringVar()
    usage_gas_data = IntVar()
    usage_water_data = IntVar()
    usage_elec_data = IntVar()

    # define entry fields
    entry_date_data = Entry(window2,textvariable=usage_date_data,width=9)
    entry_date_data.insert(0, 'mm/dd/yy')
    entry_date_data.bind("<FocusIn>", lambda args: entry_date_data.delete('0', 'end'))

    entry_gas_data = Entry(window2,textvariable=usage_gas_data,width=9)
    entry_gas_data.bind("<FocusIn>", lambda args: entry_gas_data.delete('0', 'end'))

    entry_water_data = Entry(window2,textvariable=usage_water_data,width=9)
    entry_water_data.bind("<FocusIn>", lambda args: entry_water_data.delete('0', 'end'))

    entry_elec_data = Entry(window2,textvariable=usage_elec_data,width=9)
    entry_elec_data.bind("<FocusIn>", lambda args: entry_elec_data.delete('0', 'end'))

    #define buttons
    add_data_button = Button(window2,text="Add data", command= save_data)
    close_button = Button(window2,text="close", command=window_close)

    # place all the things on the grid
    #---row 0---
    label_date.grid (row=0,column=0)
    label_gas.grid (row=0,column=1)
    label_water.grid (row=0,column=2)
    label_elec.grid (row=0,column=3)

    #---row 1---
    entry_date_data.grid (row=1,column=0)
    entry_gas_data.grid (row=1,column=1)
    entry_water_data.grid (row=1,column=2)
    entry_elec_data.grid (row=1,column=3)

    #---row 2---
    add_data_button.grid (row=2,column=0,columnspan=2,stick=W)    
    close_button.grid (row=2,column=3, stick=E)


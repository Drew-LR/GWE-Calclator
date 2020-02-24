from tkinter import *
import usage_data_lib, close_program_lib, all_data_lib, yesterday_lib, date_data

# instantiate window    
window = Tk()
window.title ("GWE Calculator")

# define variables
gas_data = StringVar()
water_data = StringVar()
elec_data = StringVar()

# define functions

def print_all():

    def window_close():
        window3.destroy()

    window3 = Toplevel()
    window3.title ("All Data Output")

    printout1 = StringVar()
    printout2 = StringVar()
    printout3 = StringVar()

        # text area1
    text_area1 = Label(window3,textvariable = printout1,bg="white",width=50,anchor=W)
    text_area1.grid (row=0, column=0, padx=1,pady=1)
        # text area2
    text_area2 = Label(window3,textvariable = printout2,bg="white",width=50,anchor=W)
    text_area2.grid (row=1, column=0, padx=1,pady=1)
        # text area3
    text_area3 = Label(window3,textvariable = printout3,bg="white",width=50,anchor=W)
    text_area3.grid (row=2, column=0, padx=1,pady=1)

    # close button
    close_button = Button(window3,text="close", command= window_close)
    close_button.grid (row=3,column=0,stick=E)

    file = open('GWE_data.txt', 'r')
    lines = file.readlines()
    file.close()
    first_line = lines[0].split()
    last_line = lines[-1].split()
    
    gas_usage = (float(last_line[1]) - float(first_line[1])) * float(line[0])
    water_usage = (float(last_line[2]) - float(first_line[2])) * float(line[1])
    elec_usage = (float(last_line[3]) - float(first_line[3])) * float(line[2])

    printout1 = printout1.set('Gas usage from '+first_line[0]+' to '+last_line[0]+' was '+str(round(gas_usage, 2))+' euros.')
    printout2 = printout2.set('Water usage from '+first_line[0]+' to '+last_line[0]+' was '+str(round(water_usage, 2))+' euros.')
    printout3 = printout3.set('Electricity usage from '+first_line[0]+' to '+last_line[0]+' is '+str(round(elec_usage, 2))+' euros.')




def save_cost_data(a,b,c):
    entered_gas_cost = a
    entered_water_cost = b
    entered_elec_cost = c

    file = open('cost_doc.txt', 'w')
    file.write (str(entered_gas_cost)+' ')
    file.write (str(entered_water_cost)+' ')
    file.write (str(entered_elec_cost)+' ')

# define widgets

# define labels
    # enter cost label
label_cost = Label(window,text="Enter price per unit:") #prompt user for cost of GWE
label_cost.grid (row=0,column=0,stick=W)

    # gas label
label_gas = Label(window,text="Gas:")
label_gas.grid (row=0,column=1,stick=E)

    # water label
label_water = Label(window,text="Water:")
label_water.grid (row=1,column=1,stick=E)

    # elec label
label_elec = Label(window,text="Elec:")
label_elec.grid (row=2,column=1,stick=NE)

    #gas unit label
label_gas_unit = Label(window,text="m3")
label_gas_unit.grid (row=0,column=3,stick=W)

    # water unit label
label_water_unit = Label(window,text="m3")
label_water_unit.grid (row=1,column=3,stick=W)

    # elec unit label
label_elec_unit = Label(window,text="kWh")
label_elec_unit.grid (row=2,column=3,stick=NW)

    # print data label
label_data = Label(window,text="Print data:")
label_data.grid (row=0,column=4,stick=E)

# define entry fields
    # gas entry
entry_gas = Entry(textvariable=gas_data,width=9) #text feilds for GWE
entry_gas.insert(0, '0')
entry_gas.bind("<FocusIn>", lambda args: entry_gas.delete('0', 'end'))
entry_gas.grid (row=0,column=2,stick=E)

    # water entry
entry_water = Entry(textvariable=water_data,width=9)
entry_water.insert(0, '0')
entry_water.bind("<FocusIn>", lambda args: entry_water.delete('0', 'end'))
entry_water.grid (row=1,column=2,stick=E)

    # elec entry
entry_elec = Entry(textvariable=elec_data,width=9)
entry_elec.insert(0, '0')
entry_elec.bind("<FocusIn>", lambda args: entry_elec.delete('0', 'end'))
entry_elec.grid (row=2,column=2,stick=NE)

# define buttons

    # all data button
all_button = Button(window,text="All data",padx=38, command=print_all)
all_button.grid (row=0,column=5,stick=N,rowspan=2)

    # yesterdays data button
yester_button = Button(window,text="Yesterdays data", command=lambda: yesterday_lib.print_yesterday(line))
yester_button.grid (row=1,column=5,stick=NW,rowspan=2,pady=7)

    # from date button
date_button = Button(window,text="Data from date", padx=14, command=lambda: date_data.date_select(line))
date_button.grid (row=2,column=5,stick=N,rowspan=2,pady=14)

    # update cost button
add_cost_button = Button(window, text="Update costs", command=lambda: save_cost_data(entry_gas.get(),entry_water.get(),entry_elec.get()))
add_cost_button.grid (row=2,column=0,stick=NW)

    # add data button
add_data_button = Button(window,text="Input new data", command=usage_data_lib.add_data_win)
add_data_button.grid (row=6,column=0,stick=W)

    # close button
close_button = Button(window, text="close", command=close_program_lib.close_program)
close_button.grid (row=6,column=5,stick=E)

window.grid_rowconfigure(5,minsize=5)

# begin by pre-loading any saved data
file = open('cost_doc.txt', 'r')
line = file.readline()
file.close()
if line != '':
    line=line.split()
    gas_data = gas_data.set(line[0])
    water_data = water_data.set(line[1])
    elec_data = elec_data.set(line[2])
elif line == '':
    pass


window.mainloop()
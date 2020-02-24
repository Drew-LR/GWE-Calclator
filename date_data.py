from tkinter import *

def date_select(a):

    def window_close():
            window6.destroy()

    def print_date(a, date):
        def window_close():
            window5.destroy()

        window5 = Toplevel()
        window5.title ("Output Period")

        printout1 = StringVar()
        printout2 = StringVar()
        printout3 = StringVar()

            # text area1
        text_area1 = Label(window5,textvariable = printout1,bg="white",width=50,anchor=W)
        text_area1.grid (row=0, column=0, padx=1,pady=1)
            # text area2
        text_area2 = Label(window5,textvariable = printout2,bg="white",width=50,anchor=W)
        text_area2.grid (row=1, column=0, padx=1,pady=1)
            # text area3
        text_area3 = Label(window5,textvariable = printout3,bg="white",width=50,anchor=W)
        text_area3.grid (row=2, column=0, padx=1,pady=1)

        # close button
        close_button = Button(window5,text="close", command= window_close)
        close_button.grid (row=3,column=0,stick=E)

        file = open('GWE_data.txt', 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            if date[1] in line:
                line_1 = line.split() # Date_2 becomes line_1 because usage on the second
            if date[0] in line:        # date is subtracted from usage on the first date.
                line_2 = line.split() # i.e. line_1[x] - line_2[x] * $/pu = usage cost

        g_usage = (float(line_1[1]) - float(line_2[1])) * float(a[0])
        w_usage = (float(line_1[2]) - float(line_2[2])) * float(a[1])
        e_usage = (float(line_1[3]) - float(line_2[3])) * float(a[2])
        
        printout1 = printout1.set ('Gas usage for the period '+date[0]+' to '+date[1]+' was '+str(round(g_usage,2))+' euros.')
        printout2 = printout2.set ('Gas usage for the period '+date[0]+' to '+date[1]+' was '+str(round(w_usage,2))+' euros.')
        printout3 = printout3.set ('Gas usage for the period '+date[0]+' to '+date[1]+' was '+str(round(e_usage,2))+' euros.')

    window6 = Toplevel()
    window6.title ("Enter Date")

    entry_1 = Label(window6,text='From: ')
    entry_1.grid(row=0,column=1,stick=E) 
    date_1 = Entry(window6)
    date_1.grid(row=0,column=2)

    entry_2 = Label(window6,text='To: ')
    entry_2.grid(row=1,column=1,stick=E) 
    date_2 = Entry(window6)
    date_2.grid(row=1,column=2)

    button = Button(window6,text="Print", command=lambda: print_date(a, [date_1.get(), date_2.get()]))
    button.grid(row=2,column=1)   

    close_button = Button(window6,text='close', command=window_close)
    close_button.grid(row=2,column=2,stick=E) 

    

    
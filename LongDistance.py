# LongDistance
# Nathan Szeto
# CIS156
import tkinter
# these functions will calculate the price and display the answer in a window
def evening_price():
    global minute_entry
    price = float(minute_entry.get()) * 0.12 # $0.12 is the rate for the the evening plan
    result_window = tkinter.Tk()
    total_label = tkinter.Label(result_window,
                                text = f"Your total payment will be: ${price}0")
    total_label.pack()
def off_peak_price():
    global minute_entry
    price = float(minute_entry.get()) * 0.05 # $0.05 is the rate for the the off peak plan
    result_window = tkinter.Tk()
    total_label = tkinter.Label(result_window,
                                text = f"Your total payment will be: ${price}0")
    total_label.pack()
def day_price():
    global minute_entry
    price = float(minute_entry.get()) * 0.07 # $0.70 is the rate for the the daytime plan
    rounded_price =  round(price, 3)
    result_window = tkinter.Tk()
    total_label = tkinter.Label(result_window,
                                text = f"Your total payment will be: ${rounded_price}")
    total_label.pack()
def second_step():
    second_window = tkinter.Tk()
    top_frame = tkinter.Frame(second_window)
    middle_frame = tkinter.Frame(second_window)
    bottom_frame = tkinter.Frame(second_window)
    detail_label = tkinter.Label(top_frame,
                                 text = 'Enter the ammount of time you will use in minutes:')
    global minute_entry # Needs to be global so it can be accessed by the *_price functions
    minute_entry = tkinter.Entry(middle_frame,
                                 width=15)
    option = radio_value.get()
    if option ==1:
        enter_button = tkinter.Button(bottom_frame,
                                     text = 'Enter',
                                     command = day_price # next step is the function for a new window
                                     )
    elif option ==2:
        enter_button = tkinter.Button(bottom_frame,
                                     text = 'Enter',
                                     command = evening_price # next step is the function for a new window
                                     )
    elif option ==3:
        enter_button = tkinter.Button(bottom_frame,
                                     text = 'Enter',
                                     command = off_peak_price # next step is the function for a new window
                                     )
    else:
        print('broken')
    cancel_button = tkinter.Button(bottom_frame,
                               text = 'Cancel',
                               command = second_window.destroy)
    
    
    detail_label.pack()
    minute_entry.pack()
    cancel_button.pack(side='left')
    enter_button.pack(side = 'right')
    top_frame.pack()
    middle_frame.pack()
    bottom_frame.pack()
    tkinter.mainloop()
    
main_window = tkinter.Tk() # main window

top_frame = tkinter.Frame(main_window) # frames of main window

bottom_frame =tkinter.Frame(main_window)

# Make radiobuttons
# When you select a radio button, it will give you a value in return, use the value to make decisions
radio_value = tkinter.IntVar() # this will track the radio button you use
rb1 = tkinter.Radiobutton(top_frame,
                          text = 'Daytime (6:00 AM through 5:59 PM)',
                          variable = radio_value,
                          value = 1)
rb2 = tkinter.Radiobutton(top_frame,
                          text = 'Evening (6:00 PM through 11:59 PM)',
                          variable = radio_value,
                          value = 2)
rb3 = tkinter.Radiobutton(top_frame,
                          text = 'Off-Peak (midnight through 5:59 AM)',
                          variable = radio_value,
                          value = 3)
continue_button = tkinter.Button(bottom_frame,
                                 text = 'Contiune',
                                 command = second_step # next step is the function for a new window
                                 )
cancel_button = tkinter.Button(bottom_frame,
                               text = 'Cancel',
                               command = main_window.destroy)
# pack radiobuttons into frames
rb1.pack()
rb2.pack()
rb3.pack()
# pack buttons
continue_button.pack(side ='right')
cancel_button.pack(side = 'left')
# pack frames into the window
top_frame.pack()
bottom_frame.pack()

# keeps the window going
tkinter.mainloop()
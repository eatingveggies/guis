#JoesAuto
# Nathan Szeto
# CIS 156

import tkinter

# Prices to the services
#OIL_CHANGE = 30.0
#LUBE_JOB = 20.0
#RADIATOR_FLUSH = 40.0
#RANSMISSION_FLUSH = 100.0
#INSPECTION = 35.0
#MUFFLER_REPLACEMENT = 200.0
#TIRE_ROTATION = 20.0
total_cost = 0.0
class MyGUI:
    def __init__(self):
        def clear():
            global total_cost # use global so we modify the total cost globally
            # The clear button will clear out the total cost and enable the enter button
            # Clear will also deselect the checkboxes and enable the buttons
            self.enter_button.configure(state = 'normal')
            self.total_cost_label.destroy()
            total_cost = 0.0
            self.check_oil.deselect()
            self.check_lube.deselect()
            self.check_radiator.deselect()
            self.check_transmission.deselect()
            self.check_inspection.deselect()
            self.check_muffler.deselect()
            self.check_tire.deselect()
            
            # Enable the Disabled buttons
            self.enter_button.configure(state='normal')
            self.check_oil.configure(state = 'normal')
            self.check_lube.configure(state = 'normal')
            self.check_radiator.configure(state = 'normal')
            self.check_transmission.configure(state = 'normal')
            self.check_inspection.configure(state = 'normal')
            self.check_muffler.configure(state = 'normal')
            self.check_tire.configure(state = 'normal')
        def calculate_price():
            # cacluclate price will calculate the price and then disable the checkboxes
            # will also disable the enter button
            global total_cost
            # All these if statements are the calculation part
            # if the checkboxes are checked, they return 1
            if self.cb_var1.get() == 1:
                total_cost += 30.0
            if self.cb_var2.get() == 1:
                total_cost += 20.0
            if self.cb_var3.get() == 1:
                total_cost += 40.0
            if self.cb_var4.get() == 1:
                total_cost += 100.0
            if self.cb_var5.get() == 1:
                total_cost += 35.0
            if self.cb_var6.get() == 1:
                total_cost += 200.0
            if self.cb_var7.get() == 1:
                total_cost += 20.0
            self.total_cost_label = tkinter.Label(self.middle_frame,
                                          text = f"total cost: {total_cost}")
            self.total_cost_label.pack()
            
            # Disable the buttons after the enter button is pressed
            self.enter_button.configure(state='disabled')
            self.check_oil.configure(state = 'disabled')
            self.check_lube.configure(state = 'disabled')
            self.check_radiator.configure(state = 'disabled')
            self.check_transmission.configure(state = 'disabled')
            self.check_inspection.configure(state = 'disabled')
            self.check_muffler.configure(state = 'disabled')
            self.check_tire.configure(state = 'disabled')
            
            
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Set up intvar objects to be used with check buttons
        # an intvar object used to associate a button to an integer
        # This is useful because we can use if statements for each button
        # So each check box is its own if statement (if this box is checked,
        # perform a function)
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        
        # we will set the IntVar() objects to 0 or turn them off
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        
        # Make the title
        self.title = tkinter.Label(self.top_frame,
                                   text = "Welcome to Joe's Auto, please select the services you need.")
        
        # Make the Check buttons
        self.check_oil = tkinter.Checkbutton(self.top_frame,
                                     text = 'Oil Change',
                                     variable = self.cb_var1) 
        self.check_lube = tkinter.Checkbutton(self.top_frame,
                                     text = 'Lube Job',
                                     variable = self.cb_var2) 
        self.check_radiator = tkinter.Checkbutton(self.top_frame,
                                     text = 'Radiator Flush',
                                     variable = self.cb_var3) 
        self.check_transmission = tkinter.Checkbutton(self.top_frame,
                                     text = 'Transmission Flush',
                                     variable = self.cb_var4) 
        self.check_inspection = tkinter.Checkbutton(self.top_frame,
                                     text = 'Inspection',
                                     variable = self.cb_var5) 
        self.check_muffler = tkinter.Checkbutton(self.top_frame,
                                     text = 'Muffler Replacement',
                                     variable = self.cb_var6) 
        self.check_tire = tkinter.Checkbutton(self.top_frame,
                                     text = 'Tire Rotation',
                                     variable = self.cb_var7) 
        self.enter_button = tkinter.Button(self.bottom_frame,
                                           text = 'Enter',
                                           command = calculate_price)
        self.clear_button = tkinter.Button(self.bottom_frame,
                                           text = 'Clear',
                                           command = clear)
        
        # packing the check boxes
        self.title.pack()
        self.check_oil.pack()
        self.check_lube.pack()
        self.check_radiator.pack()
        self.check_transmission.pack()
        self.check_inspection.pack()
        self.check_muffler.pack()
        self.check_tire.pack()
        
        # packing buttons, use side to choose where they appear in the bottom frame
        self.enter_button.pack(side = 'right')
        self.clear_button.pack(side = 'left')
        
        # packing frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        # loop the gui
        self.main_window.mainloop()
        
# create an instance of myGUI (execute it)
mygui = MyGUI()
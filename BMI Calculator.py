#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Pavishaan Vijeyarajah 100874494
from tkinter import  *

class BMI_Calculator:
    
    def __init__(self):
        window = Tk() #window for the program
        window.title("BMI Calculator") #title of the window
        frame1 = Frame(window) #frame of the window
        frame1.grid(row=1, column=1) #setting the row and column of the frame 
        Label(frame1, text = "Height (m):").grid(row = 1, column = 3) #creates a label for the height
        self.v1 = StringVar() #uses v1 to store the height
        Entry(frame1,textvariable=self.v1).grid(row = 1, column = 4, padx = 5, pady = 5)#creates an textbox for user to type height
        Label(frame1, text = "Weight(kg):").grid(row = 2, column = 3) #creates a label for weight
        self.v2 = StringVar() #uses v2 to store weight
        Entry(frame1,textvariable=self.v2).grid(row = 2, column = 4, padx = 5, pady = 5) #creates a textbox for user to type weight
        self.bmi_value = StringVar() #uses bmi_value to store result
        Label(frame1,textvariable=self.bmi_value).grid(row=3,column=4) #creates a label for the calculated bmi
        btCalc = Button(frame1, text = "Start Calculate!",command=self.calculate_bmi_number).grid(row=4,column=4) #creates a button that calculates bmi on click
        window.mainloop() #loops Tkinter event
    #uses the bmi formula to calculate using width and height
    #sends the value to get_bmi_status_description to check the bmi level 
    def calculate_bmi_number(self):
        bmi_value=self.bmi_value.set(eval(self.v2.get()) / (eval(self.v1.get())*eval(self.v1.get())))#gets the values stored in the weight and height and sets it to the result
        get_bmi_status_description(bmi_value)
    #uses bmi from calculation to describe the bmi level
    def get_bmi_status_description(self,bmi_value):
        if bmi_value<5:#checks if bmi is over 5
            return "Underweight"
        elif bmi_value>=5 and bmi_value<24.9:#checks if bmi is between 5 and 24.9
            return "Healthy Weight"
        elif bmi_value>=25:#checks if bmi is over 25 (9 in lab slides might be typo)
            return "Overweight"
BMI_Calculator()


# In[ ]:





# In[ ]:





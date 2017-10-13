# Created by: Jenny Trac
# Created on: Oct 13 2017
# Program determines if a year is a leap year

import ui

def check_touch_up_inside(sender):
    # checks if year is a leap year
    
    year = int(view['year_textfield'].text)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                view['answer_label'].text = "It is a leap year."
            else:
                view['answer_label'].text = "It is not a leap year."
        else:
            view['answer_label'].text = "It is a leap year."
    else:
            view['answer_label'].text = "It is not a leap year."

view = ui.load_view()
view.present('sheet')

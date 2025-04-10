import tkinter.font
import RPi.GPIO as IO
import time
IO.setmode(IO.BCM)
IO.setup(4,IO.OUT)
IO.setup(5,IO.OUT)
IO.setup(6,IO.OUT)

win = Tk()
win.title("LED")
Font = tkinter.font.Font(family = "Arial", size=12, weight = "bold")
def toggle_blue():
        if  IO.input(4):
                IO.output(4, IO.LOW)
                blue_Button["text"]= "Blue LED on"
        else:
                IO.output(4,IO.HIGH)
                blue_Button["text"] = "Blue LED off"

def toggle_yellow():
        if IO.input(5):
                IO.output(5,IO.LOW)
                yellow_Button["text"] = "Yellow LED on"
        else:
                IO.output(5, IO.HIGH)
		yellow_Button["text"] = "Yellow LED off"
def toggle_red():
        if IO.input(6):
                IO.output(6, IO.LOW)
                red_Button["text"] = "Red LED on"
        else:
                IO.output(6, IO.HIGH)
                red_Button["text"] = "Red LED off"

blue_Button = Button(win, text = "Blue LED on", font = Font, command = toggle_blue, bg="white", height = 1, width = 24)
blue_Button.grid(row = 0, column = 0)

yellow_Button = Button(win, text = "Yellow LED on", font = Font, command = toggle_yellow, bg= "white", height = 1, widt>yellow_Button.grid(row = 1, column =0)

red_Button = Button(win, text = "RED LED on", font = Font, command = toggle_red, bg="white", height = 1, width = 24)
red_Button.grid(row=2, column =0)

def exit():
        win.destroy()
        IO.cleanup()
exit_Button = Button(win, text ="Exit", font = Font, command = exit, bg = "red", height = 1, width = 24)
exit_Button.grid(row = 3, column = 0)

win.protocol("WM_DELETE_WINDOW",exit)
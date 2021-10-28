from simshow import simshow
import keyboard
import sys

input_list = []
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        input_list.append(int(key))
        if len(input_list) == 7:
            if input_list == [1,2,3,4,5,6,7]:
                print("Success")
                simshow('success.png')
                input_list = []
                #sys.exit(0)
            else:
                print("Didnt work")
                #sys.exit(0)

                


        





                
       

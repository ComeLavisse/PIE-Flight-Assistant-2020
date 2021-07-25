#### Import other python files####
from __future__ import unicode_literals, print_function
import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN


from threading import Thread
import tkinter as tk
import time
import datetime as dt
import sys 
import os
import pandas as pd
import time
import speech_recognition as sr
sys.path.append(os.path.relpath("."))
from creating_entities import *
from ontology_request import *
import time
from gtts import gTTS
import gtts
from playsound import playsound

with io.open("../sample_datasets/requests_dataset.json") as f:
    sample_dataset = json.load(f)
nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
nlu_engine = nlu_engine.fit(sample_dataset)


####Getting the length of the flight####
len_flight = get_len()

#### Starting and running simulation####
def run_environment(len_flight):

    start = tk.Label(Frame1, text="Starting simulation\n")
    start.pack()

    create_ontology()
    total_time = dt.timedelta(seconds=len_flight*20)

    update = tk.Label(Frame1,text="Ontology created\n")
    update.pack()

    pilot_monitoring = tk.Text(Frame4, height = 5)
    pilot_monitoring.pack()

    start.config(text="Simulation running...")

    for i in range(1,len_flight):

        current_time = dt.timedelta(seconds=i*20)
        pilot_monitoring_text = pilot_monitoring_fun()
        if pilot_monitoring_text == "":
            pilot_monitoring_text = "All parameters OK"
        pilot_monitoring.insert(tk.END, pilot_monitoring_text)
        update_ontology(i)
        update.config(text=f"Elapsed time : ({current_time}/{total_time})")
        time.sleep(20)
        pilot_monitoring.delete('1.0', tk.END)
    tk.Label(Frame1,text="Simulation finished").pack()


####Speech recognition algorithm###

def speech_recognition():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites quelque chose")
        audio = r.listen(source)
    try:
        tic = time.perf_counter()
        text = r.recognize_google(audio)
        toc = time.perf_counter()
        print('perfo = ', toc-tic, 's')
        print("Vous avez dit : " + text)
        return("You have said : " + text)
    except sr.UnknownValueError:
        return("Audio wasn't understood")
    except sr.RequestError as e:
        return("Le service Google Speech API ne fonctionne plus" + format(e))

####Starting and printing question####
def question_print():
    tk.Label(Frame2,text="\nType below what you want to know and press enter or 'Submit' button.\n").pack()
    tk.Label(Frame2,text="What is the airport with ... ?\n").pack()
    tk.Label(Frame2,text="What is the aircraft current ... ?\n").pack()
    text = tk.Text(Frame2, height = 5)
    text.pack(side=tk.BOTTOM)

    def process_callback(*args):
        text.delete('1.0', tk.END)
        #answer = process_answer(entry.get())
        question = speech_recognition()
        #tic = time.perf_counter()
        text.insert(tk.END, question + '\n')
        answer = process_answer(question, text)
        if answer is None:
            return
        text.insert(tk.END, answer)
        Frame2.update()
        speech = gtts.gTTS(answer + ".", lang = "en", slow = False)
        print(speech)
        speech.save("tts.mp3")
        playsound("tts.mp3")
        os.remove("tts.mp3")
        #toc = time.perf_counter()
        #print('perfo = ', toc-tic, 's')
        #entry.delete(0, tk.END)

    # tk.Label(Frame2,text="you have said ->").pack()
    # entry = tk.Entry(Frame2, width=75,bg='bisque')
    # entry.pack()
    # entry.focus()
    # entry.bind("<Return>", process_callback)
    button_4 = tk.Button(Frame2, text='speak', command=process_callback)
    button_4.pack()
    
    def delete_text(*args):
        text.delete('1.0', tk.END)
        Frame2.update()
    Button_5 = tk.button(Frame2, text='speak', command=delete_text)
    Button_5.pack()
####What to do with the user input####
def process_answer(ans, text):

    answer = ans.strip().lower()

    #### TEST REQUESTS ####
    if answer == "runway_0":
        return "Airport with Runway 0 is "+print_request(test_request_1())
    elif answer == "ias":
        return "The current IAS is "+str(round(test_request_3(),1))+"kts"

    #### REAL REQUESTS ####
    #Request 12&20
    elif "altitude" in answer:
        if "waypoint" in answer:
            WP = answer.split(" ")[-1].upper()
            str_ans = print_request(request_12(WP))
            ans = float(str_ans)
            if ans >= 0:
                return f"The planned altitude at waypoint {WP} is " + str_ans +"ft."
            else:
                return f"No planned altitude for waypoint {WP}"
        elif "optimal" in answer:
            return "The optimal flight level is FL"+str(round(request_20())) + "."
        else:
            return "The current altitude is "+str(round(test_request_2(),1))+"m."
    
    #Request 6
    elif "wind speed at arrival" in answer:
        return "The wind speed at arrival is "+print_request(request_6())+"kts."
    #Request 5
    elif "wind orientation at arrival" in answer:
        return "The wind orientation at arrival is "+print_request(request_5())+"°."
    #Request 8 and 9
    elif "nearest airport" in answer:
        if "landing" in answer:
            return print_nearest_possible(request_9()) + "."
        else:
            return print_nearest_airport(request_8()) + "."
    #Request 7 15 16
    elif "weather" in answer:
        if "arrival" in answer:
            return f"The weather at arrival is" + print_weather_request(request_7()) +"."
        elif "waypoint" in answer:
            WP = answer.split(" ")[-1].upper()
            return f"The weather at waypoint {WP} is" + print_weather_request(request_15(WP)) +"."
        elif "airport" in answer:
            airport = answer.split(" ")[-1].upper()
            return f"The weather at {airport} is" + print_weather_request(request_16(airport)) +"."
    #Request 11
    elif "waypoint eta" in answer :
            return f"The ETA at the next waypoint is " + str(round(request_11(),2)) +" min."
    #Request 13
    elif "arrival eta" in answer:
            return "The ETA at arrival airport is "+str(int(print_request(request_13()))) + "."
    #Request 17
    elif "fuel remaining" in answer:
            return "The remaining fuel quantity is "+str(round((request_17()))) + "%."
    #Request 18
    elif "fuel airport" in answer:
            airport = answer.split(" ")[-1].upper()
            fuel = round(request_18(airport))
            if fuel > 0:
                return f"The remaining fuel quantity at {airport} is "+str(fuel) + "%."
            else:
                return "The airport is not reachable"
    #Request 10
    elif "mar" in answer:
        if request_10()[0].lower() == "cruise":
            return "Maximum Achivable Range is " + str(round(request_10()[1],1))+"nm"
        else:
            return "You are not in Cruise"
    #Request 14
    elif "antiicing" in answer:
        return print_icing_request(request_14()) + "."
    #Request 19
    elif "fuel waypoint" in answer:
            WP = answer.split(" ")[-1].upper()
            fuel = round(request_19(WP))
            if fuel > 0:
                return f"The remaining fuel quantity at {WP} is "+str(fuel) + "%."
            else:
                return "The waypoint is not reachable"
    #Request 2 
    elif "approach speed" in answer:
        return f"The approach speed suiting plane configuration is "+str(round(request_2())) + "kts."
    #Request 3
    elif "landing speed" in answer:
        return f"The landing speed suiting plane configuration is "+str(round(request_3())) + "kts."
    #Request 4
    elif "landing distance" in answer:
         return f"The landing distance suiting plane configuration is "+str(round(request_4())) + "m."
         
#####Request 1 inactive pour coder le processus de checklist par reconnaissance vocale#####
    
    # #Request 1
    # elif "approach checklist" in answer:
    #      return request_1()
    # elif "flight phase" in answer:
    #     return "Current flight phase: " + str(request_fp())

    #Request 21    
    elif "opening hours" in answer:
        AirportICAOCode = str(answer.split(" ")[-1].upper())
        print(AirportICAOCode)
        return request_21(AirportICAOCode)
    
    #Request 22    
    elif "CTR opening hours" in answer:
        AirportICAOCode = str(answer.split(" ")[-1].upper())
        print(AirportICAOCode)
        return request_22(AirportICAOCode)
    
    #Request 23    
    elif "fuel" in answer:
        AirportICAOCode = str(answer.split(" ")[-1].upper())
        print(AirportICAOCode)
        return request_23(AirportICAOCode)
    
    #Request 24    
    elif "width taxiway" in answer:
        AirportICAOCode = str(answer.split(" ")[-1].upper())
        print(AirportICAOCode)
        return request_24(AirportICAOCode)
    
    #Request 25    
    elif "handling" in answer:
        AirportICAOCode = str(answer.split(" ")[-1].upper())
        print(AirportICAOCode)
        return request_25(AirportICAOCode)

#####Request pour le processus de checklist via reconnaissance vocale#####
    #Request 26
    elif "checklist" in answer:
        request_26(text)
        
#####Request pour le CFDLC via reconnaissance vocale#####
    #Request 27
    elif "speak" in answer:
        Airport = str(answer.split(" ")[-1].upper())
        return request_27(Airport, text)
    
    else:
        return "Unknown command"
    

    
def request_26(t):
    cl = pd.read_csv("../csv/checklistvoicerecognition.csv", sep=';', engine='python')
    # textcheck = tk.Text(Frame2, height = 5)
    # textcheck.pack(side=tk.BOTTOM)
    t.insert(tk.END, 'approach_checklist' + '\n')
    time.sleep(2)
    for k in range (len(cl)):
        item = cl['Items'][k]
        check = cl['Check'][k]
        t.insert(tk.END, 'item :' + item + '\n' )
        t.insert(tk.END, 'You have to check and say :'+ check + '\n')
        Frame2.update()
        checkanswer = speech_recognition()
        
        while checkanswer.split(" ")[-1] not in check: 
            t.insert(tk.END, 'Wrong check, try again !' + '\n')
            Frame2.update()
            checkanswer = speech_recognition()
            
        t.insert(tk.END, checkanswer + '\n')
        t.insert(tk.END, 'Good check !' + '\n')
        Frame2.update()
        time.sleep(2)
        t.delete('1.0', tk.END)
        Frame2.update()
    t.insert(tk.END, 'checklist complete !')
    Frame2.update()
    
def request_27(Airport, text):
    Airport_list = pd.read_csv("../csv/airport.csv", sep=';', engine='python')
    for i in range (len(Airport_list)):
        Airport_name = Airport_list['AirportName'][i].split("_")[0].split("'")[1].upper()
        if Airport_name in Airport:
            frequency = str(Airport_list['AirportCTRLanding'][i])
            text.insert(tk.END,"You are speaking to " + Airport_name + " ATC on frequency " + frequency + ", say your message." + '\n')
            Frame2.update()
            message = speech_recognition()
            text.insert(tk.END, message + '\n')
            text.insert(tk.END, 'message sent !' + '\n')
            Frame2.update()
            return
    text.insert(tk.END, "Unknown Airport")
    Frame2.update()
            
    
def pilot_monitoring_fun():
    text = request_pm_1() + request_pm_2() + request_pm_3() + request_pm_4() + request_pm_5()
    return text

####Function to start simulation and questions simultaneously####
def start_question():
    Thread(target = question_print).start()
    button_2.pack_forget()

def start_simulation():
    Thread(target = run_environment, args=[len_flight]).start()
    button_1.config(text="Simulation started")
    button_1.pack_forget()
    Frame2.pack(padx=10, pady=10)
    Frame4.pack(padx=10, pady=10)
    button_2.pack()
    



#### BUILDING INTERFACE ####
import tkinter as tk
from tkinter import ttk


####Setting up Tkinter####
gui = tk.Tk()
gui.title("Dassault Aircraft Interface")


#####Building the frames####
#Frame simulation
Frame1 = tk.LabelFrame(gui,text="Simulation", height = 100, width = 100, borderwidth=2, relief=tk.GROOVE)
Frame1.pack(side=tk.TOP, padx=30, pady=30)

#Frame questions
Frame2 = tk.LabelFrame(gui, text="Questions", height = 100, width = 100, borderwidth=2, relief=tk.GROOVE)

#Frame pilot monitoring
Frame4 = tk.LabelFrame(gui, text="Pilot monitoring", height = 100, width = 300, borderwidth=2, relief=tk.GROOVE)

# frame quit
Frame3 = tk.Frame(gui, height = 100, width = 100, borderwidth=2, relief=tk.GROOVE)
Frame3.pack(side=tk.BOTTOM, padx=10, pady=10)



button_1 = tk.Button(Frame1, text="Start simulation", command=start_simulation) 
button_2 = tk.Button(Frame2, text="Start questions", command=start_question) 
button_3 = tk.Button(Frame3, text="Quit", command=gui.destroy)
button_1.pack()
button_3.pack()

####Starting the GUI####
gui.mainloop()


import wolframalpha
import pyttsx3
import wikipedia
import PySimpleGUI as sg

#API key
client = wolframalpha.Client("9WK853-HWY9X35EWU")

#pysimplegui basic example code
sg.theme('DarkPurple')
layout =[[sg.Text('say something'), sg.InputText()],[sg.Button('OK'), sg.Button('CANCEL')]]
window = sg.Window('vAssistant', layout)

#initializing text to speech lib
engine = pyttsx3.init()
#setting voice properties
engine.setProperty("rate", 125)
engine.setProperty("volume", 0.8)

#window and events
while True:
    #reads events and input value
    event, values = window.read()
    #end if cancel
    if event in (None, 'Cancel'):
        break
    try:
        #grap information from wikipedia and wolfram
        response_wiki = wikipedia.summary(values[0], sentences=2)
        response_wolfram = next(client.query(values[0]).results).text
        engine.say(wolfram_res) #text to speech
        sg.PopupNonBlocking("Wolfram Result: " + response_wolfram, "Wikipedia Result: " + response_wiki)
    #if wikipedia fails -> translate wolfram only
    except wikipedia.exceptions.DisambiguationError:
        response_wolfram = next(client.query(values[0]).results).text
        engine.say(response_wolfram)
        sg.PopupNonBlocking(response_wolfram)
    except wikipedia.exceptions.PageError:
        response_wolfram = next(client.query(values[0]).results).text
        engine.say(response_wolfram)
        sg.PopupNonBlocking(response_wolfram)
    #if wolfram fails -> say wiki data
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(response_wiki)
        sg.PopupNonBlocking(response_wiki)
    
    engine.runAndWait()

engine.stop()
window.close()
import os 

if __name__=='__main__':
    print ("welcome")
    x = input("enter the sentence ")
    # command=f"help"
    # os.system(command)
    from win32com.client import Dispatch
    speak =Dispatch("SAPI.SpVoice").Speak
    while True:
        speak(x)
        if(x=="exit"):
            speak("bye bye")
            break
        x = input("enter the sentence ")
    print ("exited")

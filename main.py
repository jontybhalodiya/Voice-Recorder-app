import tkinter as tk
import sounddevice
from scipy.io.wavfile import write
from datetime import datetime
fs = 44100 # sample rate



def recc():
    second=int(box1.get())
    label2 =tk.Label(app, text = "Recording finished!\n Check Your Folder.",font = ("Arial", 15))
    label2.place(x=10, y=90)
    record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    write(f"VOICE{str(current_time)}.wav",fs,record_voice)


app = tk.Tk()
app.title("Voice Recorder app")
app.geometry("400x400")
app.iconbitmap("jonty_dp_G1h_icon.ico")

label1 =tk.Label(app, text = "How many seconds you want to record?",font = ("Arial", 15))
label1.place(x=10, y=0)

box1 = tk.Entry(app, font = ("Arial", 15), bg="#D3D3D3")
box1.place(x=10, y=30)

button1 = tk.Button(app , font=("Arial",8),bg ="Orange",text ="Record",command=recc)
button1.place(x=265 , y= 30 , width = 80)

app.mainloop()

 
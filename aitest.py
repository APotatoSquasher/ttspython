from text_to_speech import save
import playsound
import tkinter as tk
window = tk.Tk()
entry1 = tk.Text(window,bg="light yellow",height=10,width=40)
entry1.pack()
label1 = tk.Label(window, text="Input language code").pack()
entry2 = tk.Entry(window)
entry2.insert(0, "en")
entry2.pack()

def Experiment():
    save(entry1.get("1.0", 'end'), entry2.get(), file="Hello-World.mp3")
    #print(entry2.get())
    playsound.playsound("Hello-World.mp3")
button1 = tk.Button(window, text="Say", command=Experiment).pack()#command=lambda: save(entry1.get("1.0", END), "en", file="Hello-World.mp3")).pack()
#save("El examen final es una de las pruebas más difíciles y estresantes del país, ya que determina si te gradúas de la escuela secundaria.", "es", file="Hello-World.mp3")
window.mainloop()
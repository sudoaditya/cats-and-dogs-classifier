import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from keras.models import load_model
model = load_model('./ClassifierModel.h5')
#initialise GUI
top = tk.Tk()
top.title('Cats and Dogs Image Classifier')
top.geometry('760x600')
top.configure(background='white')
label=Label(top,background='white', font=('arial',30,'bold'))
sign_image = Label(top)
def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((128,128))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    image = image/255
    pred = model.predict(image)
    if pred[0]>0.5:
        sign ="Dog"
    else:
        sign ="Cat"
    label.configure(foreground='#000000',text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
        command=lambda: classify(file_path),
   padx=10,pady=5)
    classify_b.configure(background='#465728', foreground='white',
font=('arial',12,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.30),
    (top.winfo_height()/2.30)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#465728', foreground='white',font=('arial',12,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
label1 = tk.Label(top, text="Cats and Dogs Image Classifier",
                  font=('arial',35,'bold'),width=40, height=2)
label1.configure(background='#166BA4',foreground='#000000')
label1.pack()
top.mainloop()
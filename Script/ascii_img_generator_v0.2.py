import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
#acii chars - in decending order in intensity
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    
#TKINTER
root = Tk()
root.title("ASCII IMAGE GENERATOR")
root.resizable(width=False, height=False)
#imgc = ImageTk.PhotoImage(PIL.Image.open('pic1.jpg'))
#panel = Label(image = img)
#panel.grid(row=0, column=0, columnspan=5)
tit = Label(root, text ='By: Lloyd Acha')
tit.grid(row=0, column=2)
panel = Label(root)
panel.grid(row=1, column=0, columnspan=3)

def open_conv():
    conv = Toplevel()
    conv.title('ASCII GRAPHICS')
    ins = Label(conv, text="A text file for this image has been created\non the same folder as the application")
    ins.pack()
    txt_b = Text(conv, width=120, height=120)
    txt_b.pack()
    with open("ascii_img.txt", "r") as file:
       data = file.read()
    txt_b.insert(INSERT,data)
    messagebox.showinfo("CHEERS!", "Your ASCII Graphics has been generated!")

def fileOpen():
    path_img = fd.askopenfilename(filetypes=[("Image File", ".jpg")])
    for xn in range(len(path_img)):
        x = path_img[xn]
        if x == '/':
            x_loc = xn+1
    path = path_img[x_loc:]
    entry_b.insert(0,str(path))
                 
#resize image
def resize_img(image, new_width=120):
    width, height = image.size
    img_ratio =  height/width
    new_height = int(new_width * img_ratio)
    rez_img = image.resize((new_width, new_height))
    return rez_img

#conver to grayscale
def grayify(image):
    grayscale_img = image.convert("L")
    return grayscale_img

#convert pixels to string
def p_to_a(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return chars

def main(new_width = 120):
    #attemp to open image
    path = fd.askopenfilename(filetypes=[("Image File", ".jpg")])
    print(path)
    for xn in range(len(path)):
        x = path[xn]
        if x == '/':
            path = path[:xn] + "\\\\" + path[xn+1:]
    imgc = ImageTk.PhotoImage(PIL.Image.open(path))
    panel.configure(image=imgc)
    panel.Image = imgc
    print(path)    
    try:
        image = PIL.Image.open(path)
    except:
        entry_b.insert(0,"not valid")
        print(path, "is not valid")

    #convert image to ascii
    new_image_data = p_to_a(grayify(resize_img(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_img = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    #print
    #print(ascii_img)

    #save
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_img)
    open_conv()
        
img_btn = Button(text="Choose an Image", width=30, command= main)
img_btn.grid(row=0,column=0)
#main()
root.mainloop()

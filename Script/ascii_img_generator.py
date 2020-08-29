import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog as fd
#acii chars - in decending order in intensity
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    
#TKINTER
root = Tk()
root.title("ASCII IMAGE GENERATOR")
#imgc = ImageTk.PhotoImage(PIL.Image.open('pic1.jpg'))
#panel = Label(image = img)
#panel.grid(row=0, column=0, columnspan=5)
tit = Label(root, text ='Created By: Lloyd Acha')
tit.grid(row=0, column=2)
panel = Label(root)
panel.grid(row=1, column=0, columnspan=3)


def fileOpen():
    path_img = fd.askopenfilename(filetypes=[("Image File", ".jpg")])
    for xn in range(len(path_img)):
        x = path_img[xn]
        if x == '/':
            x_loc = xn+1
    path = path_img[x_loc:]
    entry_b.insert(0,str(path))
                 
#resize image
def resize_img(image, new_width=100):
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

def main(new_width = 100):
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
    with open("../ASCII File/ascii_img.txt", "w") as f:
        f.write(ascii_img)
        
img_btn = Button(text="Choose an Image Dear", width=30, command= main)
img_btn.grid(row=0,column=0)
#main()
root.mainloop()

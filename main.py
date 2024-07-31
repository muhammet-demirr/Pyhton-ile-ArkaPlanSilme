from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from rembg import remove
import os


selected_input_path = None

def get_location_image():
    global selected_input_path
    input_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if input_path:
        my_image_entry.delete(0, END)
        my_image_entry.insert(0, input_path)
        selected_input_path = input_path
    return input_path

def put_location_image():
    output_place = filedialog.askdirectory()
    if output_place:
        my_bg_image_entry.delete(0, END)
        my_bg_image_entry.insert(0, output_place)

def backgroundRemove():
    if len(my_image_entry.get()) == 0 or len(my_bg_image_entry.get()) == 0:
        status_label.config(text="Please enter all info!")
    else:
        global selected_input_path
        if selected_input_path:
            extension = os.path.splitext(selected_input_path)[-1]
            output_path = selected_input_path.replace(extension, ".png")
            try:
                with open(selected_input_path, 'rb') as i:
                    with open(output_path, 'wb') as o:
                        input_file = i.read()
                        output_file = remove(input_file)
                        o.write(output_file)

                # Resmi output_place'e taşıyın
                output_filename = os.path.basename(output_path)
                output_location = os.path.join(my_bg_image_entry.get(), output_filename)
                os.rename(output_path, output_location)
                status_label.config(text="Background removed and saved successfully.")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}")
        else:
            status_label.config(text="Please select an input image first.")


my_window = Tk()
my_window.title("Background Remover")
my_window.minsize(width=300,height=200)
my_window.configure(background="gray")

my_icon = PhotoImage(file='bgicon.jpg')
my_window.iconphoto(False, my_icon)


my_img = Image.open("bgremove.jpg")
new_width = 150
new_height = 100
my_img = my_img.resize((new_width, new_height))
tk_img = ImageTk.PhotoImage(my_img)
label = Label(my_window, image=tk_img)
label.grid(row=0, column=0, columnspan=2)
label.config(border=0)


my_image_label = Label(text="Select the Picture")
my_image_label.grid(row=1, column=0, sticky="w")
my_image_label.config(background="gray")

my_image_entry = Entry(width=30)
my_image_entry.grid(row=1, column=1)
my_image_entry.config(background="black",foreground="white")

my_button_icon = Image.open("buttonicon.jpg")
second_width = 20
second_height = 20
my_button_icon = my_button_icon.resize((second_width,second_height))
tk_icon = ImageTk.PhotoImage(my_button_icon)

my_location_button = Button(image=tk_icon,command=get_location_image)
my_location_button.grid(row=1, column=2)
my_location_button.config(border=0)

my_bg_image_label = Label(text="Select the Location")
my_bg_image_label.grid(row=2, column=0, sticky="w")
my_bg_image_label.config(background="gray")

my_bg_image_entry = Entry(width=30)
my_bg_image_entry.grid(row=2, column=1)
my_bg_image_entry.config(background="black",foreground="white")

my_button_icon_2 = Image.open("buttonicon.jpg")
second_width_2 = 20
second_height_2 = 20
my_button_icon_2 = my_button_icon_2.resize((second_width_2,second_height_2))
tk_icon_2 = ImageTk.PhotoImage(my_button_icon_2)

my_location_button_2 = Button(image=tk_icon_2,command=put_location_image)
my_location_button_2.grid(row=2, column=2)
my_location_button_2.config(border=0)

apply_button = Button(text="Apply",command=backgroundRemove)
apply_button.grid(row=3, column=0, columnspan=2)
apply_button.config(background="black",foreground="white")

status_label = Label(text="")
status_label.grid(row=4, column=0, columnspan=2)
status_label.config(background="gray")


my_window.mainloop()


import tkinter as tk
import upscale as up
import tools as t
from tkinterdnd2 import DND_FILES, TkinterDnD

def drop(event):
    files = event.data.split('} {')
    print(f"Dropped files: {files}")
    
    # Loop through each file in the list
    for file in files:
        # Your code to process each file goes here
        file = file.replace("{", "").replace("}", "")
        print(f"Processing {file}")
        # upscale each image
        newfilename = t.rename_file_with_new_path(file_path:= file, new_directory:= 'img/',  2 )
        up.upscale_image(input_path:= file, output_path:= newfilename, scale_factor:=2)


root = TkinterDnD.Tk()
root.title("UpscalerAI - by Agustin Gonzalez")
root.minsize(400,300)
root.maxsize(1600,1080)
root.iconbitmap('icons/scale.png')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (800 / 2))
y = int((screen_height / 2) - (600 / 2))
root.geometry(f"800x600+{x}+{y}")

label = tk.Label(root, text="Drag and drop image files here")
label.pack(fill=tk.BOTH, expand=True)

label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', drop)

root.mainloop()

import random
import tkinter as tk
from PIL import Image , ImageTk

class ColorShifter:
    def __init__(self,root,img_path):
        self.root=root
        self.root.title('Wacky Color Shifter')
        self.img_path=img_path

        try:
            self.original_img=Image.open(self.img_path).convert('RGB')

        except FileNotFoundError:
            print(f'Error: Could not find "{img_path}". Make sure it is in your project folder!')
            self.root.quit()
            return
        self.change_btn=tk.Button(root,text='Change Color',font=('Arial',14),command=self.update_display)
        self.change_btn.pack(pady=15)
        self.img_label=tk.Label(root)
        self.img_label.pack(pady=10)
        
        self.display_im(self.original_img)

    def randomize_channels(self):
        r,g,b=self.original_img.split()
        channel_list=[r,g,b]
        random.shuffle(channel_list)
        return Image.merge('RGB',channel_list)
    
    def display_im(self,pill_img):
        resized_img=pill_img.resize((300,300))
        self.tk_img=ImageTk.PhotoImage(resized_img)
        self.img_label.config(image=self.tk_img)

    def update_display(self):
        new_wacky_img=self.randomize_channels()
        self.display_im(new_wacky_img)

if __name__=='__main__':
    window=tk.Tk()
    app= ColorShifter(window,'/home/lenovo/Documents/project/duck.jpg')
    window.mainloop()

    
        


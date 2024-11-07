                                 Teleprompter!

Programmed with python 3.11.3 with Cursor/Anaconda Prompt. 
A simple copy paste teleprompter extremely low resource draw.
Maz font size 200 800x1000 window size. Very slow or very fast.




conda create -n NAME python=3.11

Replace NAME with what you want your virtual env named:

Hit Y and then Enter when prompted.

Activate virtual env with: conda activate NAME

conda install tk

Create a new File called: teleprompter.py

Paste following code into file and save.





import tkinter as tk
from tkinter import ttk, scrolledtext

class Teleprompter:
    def __init__(self, root):
        self.root = root
        self.root.title("Teleprompter")
        # Made the default window larger to accommodate bigger text
        self.root.geometry("1000x800")
        
        # Variables
        self.is_playing = False
        self.scroll_speed = 100
        self.font_size = 36      # Larger default font size
        
        self.create_widgets()
        
    def create_widgets(self):
        # Control Frame
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill='x', padx=5, pady=5)
        
        # Speed Control
        ttk.Label(control_frame, text="Speed:").pack(side='left', padx=5)
        self.speed_scale = ttk.Scale(control_frame, from_=20, to=500, 
                                   orient='horizontal', length=200)
        self.speed_scale.set(self.scroll_speed)
        self.speed_scale.pack(side='left', padx=5)
        
        # Font Size Control (increased to 200)
        ttk.Label(control_frame, text="Font Size:").pack(side='left', padx=5)
        self.font_scale = ttk.Scale(control_frame, from_=12, to=200, 
                                  orient='horizontal', length=200)
        self.font_scale.set(self.font_size)
        self.font_scale.pack(side='left', padx=5)
        
        # Added font size label to show current size
        self.size_label = ttk.Label(control_frame, text=f"Size: {self.font_size}")
        self.size_label.pack(side='left', padx=5)
        
        # Play/Pause Button
        self.play_button = ttk.Button(control_frame, text="Play", 
                                    command=self.toggle_play)
        self.play_button.pack(side='left', padx=5)
        
        # Reset Button
        self.reset_button = ttk.Button(control_frame, text="Reset", 
                                     command=self.reset_scroll)
        self.reset_button.pack(side='left', padx=5)
        
        # Text Widget with larger default font
        self.text_widget = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            font=('Arial', self.font_size, 'bold'),  # Added bold
            background='black',
            foreground='white'
        )
        self.text_widget.pack(expand=True, fill='both', padx=5, pady=5)
        
    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.play_button.config(text="Pause" if self.is_playing else "Play")
        if self.is_playing:
            self.scroll_text()
    
    def scroll_text(self):
        if self.is_playing:
            self.text_widget.yview_scroll(1, 'units')
            # Update speed and font size
            self.scroll_speed = self.speed_scale.get()
            new_font_size = int(self.font_scale.get())
            if new_font_size != self.font_size:
                self.font_size = new_font_size
                self.text_widget.configure(font=('Arial', self.font_size, 'bold'))
                self.size_label.config(text=f"Size: {self.font_size}")  # Update size label
            
            self.root.after(int(self.scroll_speed), self.scroll_text)
    
    def reset_scroll(self):
        self.text_widget.yview_moveto(0)
        self.is_playing = False
        self.play_button.config(text="Play")

if __name__ == "__main__":
    root = tk.Tk()
    app = Teleprompter(root)
    root.mainloop()




activate teleprompter

install tk

Run it using: python teleprompter.py

conda install pyinstaller pillow


ICON CODE:


# create_icon.py
from PIL import Image, ImageDraw
import random

# Create a new image with a random background color
size = (64, 64)
img = Image.new('RGB', size, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
draw = ImageDraw.Draw(img)

# Draw a "T" for Teleprompter
draw.text((20, 10), "T", fill='white', size=40)

# Save as icon
img.save('teleprompter_icon.ico', format='ICO')


python create_icon.py

pyinstaller --onefile --windowed --icon=teleprompter_icon.ico --name="Teleprompter Pro" teleprompter.py
----------------------------------------------------------------------------
Run the conversion by opening Anaconda Prompt in your project directory and running: build.bat

pip install auto-py-to-exe
                                      GUI Option for .exe creation.
Run it: auto-py-to-exe


Programmed by Zechariah P. 
No License, use how ever you like. 
Click to run Windows .exe File, Free teleprompter! 
Windows might say the download is not safe, but it is. 
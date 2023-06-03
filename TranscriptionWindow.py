# TranscriptionWindow.py
import tkinter as tk
from tkinter import ttk
from translatepy.translators.google import GoogleTranslate

class TranscriptionWindow:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("sub")
        self.root.attributes("-alpha", 0.8)
        self.root.configure(bg="black")

        self.root.lift()
        self.root.attributes('-topmost', True)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width // 3.5)
        window_height = screen_height // 8
        self.root.geometry(f"{window_width}x{window_height}")

        self.text_widget = tk.Text(self.root, wrap=tk.WORD, font=("Gothic", 16),
                                   bg="black", fg="white", bd=0, highlightthickness=0)
        self.text_widget.grid(padx=5, pady=5, row=0, column=0, sticky=tk.NSEW)

        self.scrollbar = ttk.Scrollbar(self.root, command=self.text_widget.yview)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.text_widget["yscrollcommand"] = self.scrollbar.set

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.update_text("", "")

    def update_text(self, text, translation_lang):
        text_to_display = ""
        gtranslate = GoogleTranslate()
        num = -2
        if len(text) < 2:
            num = -len(text)
        for i in range(num, 0, 1):
            text_to_display += text[i] + '\n'
            try:
                translated_text = str(gtranslate.translate(text[i], translation_lang))
            except:
                translated_text = ""
            text_to_display += translated_text + '\n'
            print(text_to_display)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, text_to_display)
        self.text_widget.see(tk.END)
        self.root.update()

    def mainloop(self):
        self.root.mainloop()

import tkinter as tk
from tkinter import ttk
import pyshorteners
import clipboard
from PIL import Image, ImageTk

def shorten_url():
    try:
        url = url_entry.get()
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        url_output.delete(0, tk.END)
        url_output.insert(tk.END, short_url)
        clipboard.copy(short_url)
        status_label.config(text="URL shortened and copied to clipboard!", foreground="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", foreground="red")

root = tk.Tk()
root.title("QuickSnipURL")
root.geometry("400x400")
root.resizable(False, False)

icon_image = Image.open('logo.jpg')
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 11), padding=10)
style.configure('TEntry', font=('Helvetica', 11), padding=10)
style.configure('TLabel', font=('Helvetica', 11))

url_label = ttk.Label(root, text="Enter the URL:")
url_label.pack(pady=(20, 0))
url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=5)
url_entry.focus()

shorten_button = ttk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

url_output = ttk.Entry(root, width=40)
url_output.pack(pady=5)

status_label = ttk.Label(root, text="", font=('Helvetica', 9))
status_label.pack(pady=(5, 0))

root.mainloop()

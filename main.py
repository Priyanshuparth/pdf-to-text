import tkinter as tk
from tkinter import filedialog
import PyPDF2

def extract_pdf_content():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            
            content = ""
            for page in reader.pages:
                content += page.extract_text()
    with open("text.txt","w", encoding="utf-8" ,errors="ignore") as f:
        f.write(content)



window = tk.Tk()
window.title("Product manager bot")
window.geometry("500x500")
select_button = tk.Button(window, text="Select PDF", command=extract_pdf_content)
select_button.place(x=200, y=200)



window.mainloop()

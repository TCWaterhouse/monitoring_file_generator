import tkinter as tk
from tkinter import filedialog as fd
import tkinter.messagebox
from main import main


app = tk.Tk()

app.title('Monitoring Input Generator') 
app.geometry('350x400')


def input_monitoring():
    monitoring_path = fd.askopenfilename()
    monitoring_entry.delete(1, tk.END)  # Remove current text in entry
    monitoring_entry.insert(0, monitoring_path)  # Insert the 'path'

def input_setup():
    setup_path = fd.askopenfilename()
    setup_entry.delete(1, tk.END)  # Remove current text in entry
    setup_entry.insert(0, setup_path)  # Insert the 'path'

def output_folder():
    output_directory = fd.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, output_directory)  # Insert the 'path'

def begin():
    monitoring_path = monitoring_entry.get()
    setup_path = setup_entry.get()
    output_directory = output_entry.get()
    main(monitoring_path, setup_path, output_directory)

def on_click():
    tkinter.messagebox.showinfo("Monitoring Input Generator",  "Monitoring input file generated successfully!")
    app.destroy()


top_frame = tk.Frame(app)
middle_frame = tk.Frame(app)
bottom_frame = tk.Frame(app)
line1 = tk.Frame(app, height=1, width=600, bg="grey80", relief='groove')
line2 = tk.Frame(app, height=1, width=600, bg="grey80", relief='groove')

monitoring_path = tk.Label(top_frame, text="Monitoring File Path:")
monitoring_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input_monitoring)

setup_path = tk.Label(middle_frame, text="Setup File Path:")
setup_entry = tk.Entry(middle_frame, text="", width=40)
browse2 = tk.Button(middle_frame, text="Browse", command=input_setup)

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse3 = tk.Button(bottom_frame, text="Browse", command=output_folder)

begin_button = tk.Button(bottom_frame, text="Generate Monitoring Input!", command=lambda:[begin(), on_click()])

top_frame.pack(side=tk.TOP)
line1.pack(pady=10)
middle_frame.pack()
line2.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

monitoring_path.pack(pady=5)
monitoring_entry.pack(pady=5)
browse1.pack(pady=5)

setup_path.pack(pady=5)
setup_entry.pack(pady=5)
browse2.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse3.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)


app.mainloop()
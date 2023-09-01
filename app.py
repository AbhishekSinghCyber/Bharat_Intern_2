import tkinter as tk

bg_color = "lavender"
radio_fg_color = "#0a4d68"

cyber = tk.Tk()
cyber.title("Temperature Converter App")
cyber.geometry("500x500")
cyber.resizable()
cyber.iconbitmap("temperature.ico")
cyber.config(bg=bg_color)


# Define Definition of button
def convert():
    temperature = float(entry.get())
    if var.get() == 1:
        converted_temp = (temperature * 1.8) + 32
        result_label.config(text=f"{converted_temp:.2f}℉")

    elif var.get() == 2:
        converted_temp = (temperature - 32) * 5 / 9
        result_label.config(text=f"{converted_temp:.2f}℃")

    elif var.get() == 3:
        converted_temperature = (temperature + 273.15)
        result_label.config(text=f"{converted_temperature:.2f}°K")

    elif var.get() == 4:
        converted_temperature = (temperature - 273.15)
        result_label.config(text=f"{converted_temperature:.2f}℃")

    else:
        print("Invalid Operation")


# Label
main_label = tk.Label(cyber, text='Temperature Converter App', font=('times new roman', 35, 'bold'), bg='floral white',
                      fg='royal blue')
main_label.pack(pady=20)

# Entry Label

entry_label = tk.Label(cyber, text='Enter Temperature Which You Wants To Convert',
                       font=('times new roman', 20, 'bold'), bg=bg_color, fg='black')
entry_label.pack()

# Entry
entry = tk.Entry(cyber, font=('times new roman', 22, 'bold'), bg="seashell", fg='navy', bd=12, width=21)
entry.pack(pady=20)
var = tk.IntVar()

# Create a frame for Radio Buttons

frame = tk.Frame(cyber, bg='cyan')
frame.pack(pady=15)

# Radio Buttons

# Celsius To Fahrenheit
c_to_f = tk.Radiobutton(frame, text='Celsius To Fahrenheit', variable=var, value=1, font=('times new roman', 16),
                        bg=bg_color, activebackground=bg_color, activeforeground=radio_fg_color)

c_to_f.grid(row=0, column=0)

# Fahrenheit To Celsius
f_to_c = tk.Radiobutton(frame, text='Fahrenheit To Celsius', variable=var, value=2, font=('times new roman', 16),
                        bg=bg_color, activebackground=bg_color, activeforeground=radio_fg_color)

f_to_c.grid(row=1, column=0)

# Celsius To Kelvin
c_to_k = tk.Radiobutton(frame, text="Celsius To Kelvin", variable=var, value=3, font=('times new roman', 16),
                        bg=bg_color, activebackground=bg_color, activeforeground='orange')

c_to_k.grid(row=2, column=0)

# Kelvin To Celsius
k_to_c = tk.Radiobutton(frame, text='Kelvin To Celsius', variable=var, value=4, font=('times new roman', 16),
                        bg=bg_color, activebackground=bg_color, activeforeground=radio_fg_color)

k_to_c.grid(row=3, column=0)

# Creating Convert Button
convert_button = tk.Button(cyber, text='CONVERT', font=('times new roman', 22), bg='dodger blue',
                           bd=13, width=14, command=convert)
convert_button.pack()


# Result Label
res_label = tk.Label(cyber, text='Your Converted Temperature Is :-', font=('arial', 17, 'bold'),
                     bg=bg_color, fg='black')
res_label.pack()
# Result
result_label = tk.Label(cyber, text='', font=('times new roman', 27, 'bold'), bg=bg_color, fg='blue')
result_label.pack(pady=15)

# Internship Label
internship_label = tk.Label(cyber, text='Bharat Intern Internship', font=('times new roman', 25, 'bold'),
                            bg="white", fg='orange red')
internship_label.pack(pady=40)

cyber.mainloop()

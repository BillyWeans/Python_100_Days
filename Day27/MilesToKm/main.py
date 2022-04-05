import tkinter


def convert_m_km():
    m = float(miles_input.get())
    km = round(m * 1.609,2)
    label_kms.config(text=f"{km:.2f}")


window = tkinter.Tk()
window.minsize(width=300, height=200)
window.config(padx=20, pady=30)
window.title("Miles to KMs")

label_sttc_equal_to = tkinter.Label(text="is equal to")
label_sttc_equal_to.grid(column=0, row=1)

label_sttc_miles = tkinter.Label(text="Miles")
label_sttc_miles.grid(column=2, row=0)

label_sttc_kms = tkinter.Label(text="Km")
label_sttc_kms.grid(column=2, row=1)

label_kms = tkinter.Label()
label_kms.grid(column=1, row=1)

miles_input = tkinter.Entry(width=5)
miles_input.grid(column=1, row=0)

btn_calculate = tkinter.Button(text="Calculate", command=convert_m_km)
btn_calculate.grid(column=1, row=2)

tkinter.mainloop()

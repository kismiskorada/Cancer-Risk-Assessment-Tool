import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Cancer Risk Calculator")

# Create a function to calculate the risk level
def calculate_risk():
    # Get the user's inputs
    age = int(age_entry.get())
    gender = gender_var.get()
    smoking = smoking_var.get()
    diet = diet_var.get()
    exercise = exercise_var.get()
    family_history = family_var.get()
    alcohol = alcohol_var.get()

    # Calculate the risk level
    risk_level = 0

    if age >= 50:
        risk_level += 2

    if gender == "Female":
        risk_level += 1

    if smoking == "Yes":
        risk_level += 3

    if diet == "Poor":
        risk_level += 2

    if exercise == "No":
        risk_level += 2

    if family_history == "Yes":
        risk_level += 2

    if alcohol == "Moderate":
        risk_level += 2
    elif alcohol == "Heavy":
        risk_level += 3

    # Determine risk level description
    if risk_level < 5:
        risk_desc = "low"
    elif risk_level < 9:
        risk_desc = "average"
    else:
        risk_desc = "high"

    # Display the result in a label
    result_label.config(text=f"Your risk of developing cancer is {risk_desc}.")

# Create age input
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Create gender input
gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
gender_var.set("Male")
gender_male = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
gender_male.pack()
gender_female = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
gender_female.pack()

# Create smoking input
smoking_label = tk.Label(window, text="Do you smoke?")
smoking_label.pack()
smoking_var = tk.StringVar()
smoking_var.set("No")
smoking_no = tk.Radiobutton(window, text="No", variable=smoking_var, value="No")
smoking_no.pack()
smoking_yes = tk.Radiobutton(window, text="Yes", variable=smoking_var, value="Yes")
smoking_yes.pack()

# Create diet input
diet_label = tk.Label(window, text="Do you take healthy diet?")
diet_label.pack()
diet_var = tk.StringVar()
diet_var.set("Good")
diet_good = tk.Radiobutton(window, text="Good", variable=diet_var, value="Good")
diet_good.pack()
diet_poor = tk.Radiobutton(window, text="Poor", variable=diet_var, value="Poor")
diet_poor.pack()

# Create exercise input
exercise_label = tk.Label(window, text="Do you exercise regularly?")
exercise_label.pack()
exercise_var = tk.StringVar()
exercise_var.set("Yes")
exercise_yes = tk.Radiobutton(window, text="Yes", variable=exercise_var, value="Yes")
exercise_yes.pack()
exercise_no = tk.Radiobutton(window, text="No", variable=exercise_var, value="No")
exercise_no.pack()

# Create family history input
family_label = tk.Label(window, text="Do you have a family history of cancer?")
family_label.pack()
family_var = tk.StringVar()
family_var.set("No")
family_no = tk.Radiobutton(window, text="No", variable=family_var, value="No")
family_no.pack() 
family_yes = tk.Radiobutton(window, text="Yes", variable=family_var, value="Yes")
family_yes.pack()

#Create alcohol input
alcohol_label = tk.Label(window, text="Do you consume alcohol?")
alcohol_label.pack()
alcohol_var = tk.StringVar()
alcohol_var.set("None")
alcohol_none = tk.Radiobutton(window, text="None", variable=alcohol_var, value="None")
alcohol_none.pack()
alcohol_low = tk.Radiobutton(window, text="Low", variable=alcohol_var, value="Low")
alcohol_low.pack()
alcohol_moderate = tk.Radiobutton(window, text="Moderate", variable=alcohol_var, value="Moderate")
alcohol_moderate.pack()
alcohol_high = tk.Radiobutton(window, text="High", variable=alcohol_var, value="High")
alcohol_high.pack()

#Create a button to calculate the risk level
calculate_button = tk.Button(window, text="Calculate", command=calculate_risk)
calculate_button.pack()

#Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()







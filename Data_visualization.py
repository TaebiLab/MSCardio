@author: Mohammad Muntasir Rahman
E-mail: mmr510@msstate.edu
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dataset path
base_path = "MSCardio"  

# Hide the figure before plotting
plt.ioff()
# Figure and subplots to show the SCG signal
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
fig.suptitle("SCG Signal visualization")

def load_subjects():
    """ Load the list of subjects from the dataset folder. """
    return sorted([d for d in os.listdir(base_path) if d.startswith("Subject_")])

def load_recordings(subject):
    """ Load the recordings for a selected subject. """
    subject_path = os.path.join(base_path, subject)
    if os.path.exists(subject_path):
        return sorted([d for d in os.listdir(subject_path) if d.startswith("Recording_")])
    return []

def plot_scg():
    """ Load and plot the SCG signal for the selected subject and recording. """
    subject = subject_var.get()
    recording = recording_var.get()
    
    if not subject or not recording:
        messagebox.showerror("Selection Error", "Please select both subject and recording.")
        return
    
    file_path = os.path.join(base_path, subject, recording, "scg.csv")
    
    if not os.path.exists(file_path):
        messagebox.showerror("File Error", "SCG data file not found!")
        return
    
    df = pd.read_csv(file_path)
    
    if {'time', 'x', 'y', 'z'}.issubset(df.columns):
        time = pd.to_datetime(df['time'], unit='ns')
        for ax, (axis, label) in zip(axs, [('x', 'X-axis'), ('y', 'Y-axis'), ('z', 'Z-axis')]):
            ax.clear()
            ax.plot(time, df[axis], label=label, color='b' if axis == 'x' else 'g' if axis == 'y' else 'r')
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("SCG Amplitude")
            ax.set_title(f"{label} Signal for {subject}, {recording}")
            ax.legend()
            ax.grid()
        
        fig.tight_layout()
        fig.canvas.draw()
        fig.show()
    else:
        messagebox.showerror("Data Error", "CSV file does not contain required columns (time, x, y, z).")

def update_recordings(*args):
    """ Update the recordings dropdown when a new subject is selected. """
    selected_subject = subject_var.get()
    recordings = load_recordings(selected_subject)
    
    # Clear and update recording dropdown
    recording_dropdown["values"] = recordings
    if recordings:
        recording_var.set(recordings[0])  # Select first recording by default
    else:
        recording_var.set("")  # Clear if no recordings are available

def close_window():
    """ Closes the Tkinter window. """
    root.destroy()
    plt.close(fig)
    
    
# Initialize Tkinter window
root = tk.Tk()
root.title("MSCardio SCG Signal Viewer")

# Dropdowns
subject_var = tk.StringVar()
recording_var = tk.StringVar()

# Load subjects and recordings
subjects = load_subjects()
if subjects:
    subject_var.set(subjects[0])  # Default selection
    initial_recordings = load_recordings(subjects[0])
else:
    subject_var.set("")
    initial_recordings = []

# UI Layout
ttk.Label(root, text="Select Subject:").grid(row=0, column=0, padx=10, pady=5)
subject_dropdown = ttk.Combobox(root, textvariable=subject_var, values=subjects, state="readonly")
subject_dropdown.grid(row=0, column=1, padx=10, pady=5)
subject_dropdown.bind("<<ComboboxSelected>>", update_recordings)

ttk.Label(root, text="Select Recording:").grid(row=1, column=0, padx=10, pady=5)
recording_dropdown = ttk.Combobox(root, textvariable=recording_var, values=initial_recordings, state="readonly")
recording_dropdown.grid(row=1, column=1, padx=10, pady=5)

# Button to plot SCG
plot_button = ttk.Button(root, text="Show SCG Signal", command=plot_scg)
plot_button.grid(row=2, column=0, pady=10, sticky=tk.E)

# Close button
close_button = ttk.Button(root, text="Close", command=close_window)
close_button.grid(row=2, column=1, pady=10, padx=10, sticky=tk.E)

# Run the Tkinter event loop
root.mainloop()

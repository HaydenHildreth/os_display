import platform
import os
import distro
import tkinter as tk

operating_system = platform.system()
name = os.getlogin()
distro = distro.name()

root = tk.Tk()
root.title("os finder")


os_label = tk.Label(root, text=f'OS: {operating_system}')
os_label.grid()
name_label = tk.Label(root, text=f'Username: {name}')
name_label.grid()
if operating_system == 'Linux':
    distro_label = tk.Label(root, text=f'Distribution: {distro}')
    distro_label.grid()
else:
    pass
# Test on Windows


root.mainloop()

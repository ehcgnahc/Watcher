import psutil
import GPUtil
import tkinter
import sys
import os

##get picture path
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

##get system status
def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_gpu():
    return GPUtil.getGPUs()[0].load*100, GPUtil.getGPUs()[0].temperature

def get_memory():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

# def get_network():
#     net_io = psutil.net_io_counters()
#     return net_io.bytes_sent/1000000, net_io.bytes_recv/1000000

##update system status
def get_status():
    cpu = get_cpu()
    gpu= get_gpu()
    memory = get_memory()
    disk = get_disk()
    # bytes_sent, bytes_recv = get_network()

    cpu_label.config(text=f"CPU: {cpu}% N/A °C")
    gpu_label.config(text=f"GPU: {gpu[0]}% {gpu[1]}°C")
    memory_label.config(text=f"RAM: {memory}%")
    disk_label.config(text=f"DISK: {disk}%")
    # bytes_sent_label.config(text=f"封包發送: {bytes_sent} MB")
    # bytes_recv_label.config(text=f"封包接收: {bytes_recv} MB")

    window.after(1000, get_status) 

##create window
window = tkinter.Tk()
window.title("系統監控")
window.geometry("300x200")
window.resizable(False, False)
window.attributes("-topmost", True)
window.attributes("-alpha", 0.5)
window.attributes("-disabled", True)
window.attributes("-transparentcolor", "black")
#window.iconbitmap("icon.ico")
window.overrideredirect(True)

##transparent background
background_image = tkinter.PhotoImage(file=resource_path("background.png"))
background_label = tkinter.Label(window, image=background_image, bg="black")
background_label.place(x=0, y=0)

cpu_label = tkinter.Label(window, text="CPU : ", font=("Arial", 16, "bold"), anchor='w',bg="black", fg="pink")
cpu_label.place(x=10,y=10)
gpu_label = tkinter.Label(window, text="GPU : ", font=("Arial", 16, "bold"), anchor='w', bg="black", fg="pink")
gpu_label.place(x=10,y=34)
memory_label = tkinter.Label(window, text="RAM : ", font=("Arial", 16, "bold"), anchor='w', bg="black", fg="pink")
memory_label.place(x=10,y=58)
disk_label = tkinter.Label(window, text="DISK : ", font=("Arial", 16, "bold"), anchor='w', bg="black", fg="pink")
disk_label.place(x=10,y=82)
# bytes_sent_label = tkinter.Label(window, text="封包發送 : ", font=("Arial", 16), anchor='w', bg="black", fg="pink")
# bytes_sent_label.place(x=10,y=108)
# bytes_recv_label = tkinter.Label(window, text="封包接收 : ", font=("Arial", 16), anchor='w', bg="black", fg="pink")
# bytes_recv_label.place(x=10,y=132)

get_status()

window.mainloop()
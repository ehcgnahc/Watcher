import psutil
import tkinter

##get system status
def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_memory():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

def get_network():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

##update system status
def get_status():
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()
    bytes_sent, bytes_recv = get_network()

    cpu_label.config(text=f"CPU   使用率: {cpu}%")
    memory_label.config(text=f"記憶體使用率: {memory}%")
    disk_label.config(text=f"硬碟  使用率: {disk}%")
    bytes_sent_label.config(text=f"封包發送: {bytes_sent} Bytes")
    bytes_recv_label.config(text=f"封包接收: {bytes_recv} Bytes")

    window.after(1000, get_status) 

##create window
window = tkinter.Tk()
window.title("系統監控")
window.geometry("300x200")
window.resizable(False, False)
window.attributes("-topmost", True)
window.attributes("-alpha", 0.8)
#window.iconbitmap("icon.ico")
window.overrideredirect(True)

background_image = tkinter.PhotoImage(file="background.png")
background_label = tkinter.Label(window, image=background_image)
background_label.place(x=0, y=0)
cpu_label = tkinter.Label(window, text="CPU   使用率: ", font=("Arial", 12), bg="white", fg="black")
cpu_label.pack()
memory_label = tkinter.Label(window, text="記憶體使用率: ", font=("Arial", 12), bg="white", fg="black")
memory_label.pack()
disk_label = tkinter.Label(window, text="硬碟  使用率: ", font=("Arial", 12), bg="white", fg="black")
disk_label.pack()
bytes_sent_label = tkinter.Label(window, text="封包發送: ", font=("Arial", 12), bg="white", fg="black")
bytes_sent_label.pack()
bytes_recv_label = tkinter.Label(window, text="封包接收: ", font=("Arial", 12), bg="white", fg="black")
bytes_recv_label.pack()

get_status()

window.mainloop()
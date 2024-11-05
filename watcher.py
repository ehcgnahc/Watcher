import psutil
import time
import tkinter

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_memory():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

def get_network():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def get_status():
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()
    bytes_sent, bytes_recv = get_network()
    return cpu, memory, disk, bytes_sent, bytes_recv

window = tkinter.Tk()
window.title("系統監控")
window.geometry("300x200")
window.resizable(False, False)
window.iconbitmap("icon.ico")

cpu_label = tkinter.Label(window, text="CPU   使用率: ", font=("Arial", 12), bg="white", fg="black")
cpu_label.pack()

window.mainloop()

while True:
    
    print(f"CPU   使用率: {cpu}%")
    print(f"記憶體使用率: {memory}%")
    print(f"硬碟  使用率: {disk}%")
    print(f"封包發送: {bytes_sent} Bytes")
    print(f"封包接收: {bytes_recv} Bytes")
    print("-" * 30)
    
    #time.sleep(1)

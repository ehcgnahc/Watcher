import psutil
import time

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_memory():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

def get_network():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

while True:
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()
    bytes_sent, bytes_recv = get_network()
    
    print(f"CPU   使用率: {cpu}%")
    print(f"記憶體使用率: {memory}%")
    print(f"硬碟  使用率: {disk}%")
    print(f"封包發送: {bytes_sent} Bytes")
    print(f"封包接收: {bytes_recv} Bytes")
    print("-" * 30)
    
    #time.sleep(1)

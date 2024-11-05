import tkinter as tk

try:
    window = tk.Tk()
    window.title('GUI')
    window.geometry('380x400')
    window.resizable(False, False)
    
    # Prevent the window from closing immediately
    def on_closing():
        print("Window closed")
        window.destroy()
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
except Exception as e:
    print(f"發生錯誤：{e}")

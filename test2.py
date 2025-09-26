import ctypes
p = r"C:\Users\craig\AppData\Local\Programs\Python\Python312\Lib\site-packages\flexhash\_flexhash.cp312-win_amd64.pyd"
try:
    h = ctypes.WinDLL(p)   # will raise if LoadLibrary fails
    addr = ctypes.windll.kernel32.GetProcAddress(h._handle, b"PyInit__flexhash")
    print("GetProcAddress(PyInit__flexhash) ->", addr)
except Exception as e:
    print("Load or lookup failed:", e)
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast(
    "WATER REMINER",
    "Hey buddy DRINk",
    duration = 20,
    icon_path = "E:/AK_programs/.vscode/PYTHON/IMGES_files/water.ico",
    threaded = True,
)
import psutil
import time
import os
from termcolor import colored
import sys

input("Start(ENTER)\n")


sys.stdout.write("\x1b[1A" + "\x1b[1A") 
sys.stdout.write("\x1b[2K") 

warning = colored("\x1B[3mDO NOT CLOSE THIS WINDOW!\x1B[0m", "red")


print("============================================= Pc Shut Down after Download =============================================\n\n" + "\nPc shuts down, when Download Speed hits 0\n" + warning + "\n")

UPDATE_DELAY = 1 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# get the network I/O stats from psutil
io = psutil.net_io_counters()
# extract the total bytes sent and received
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv


while True:
    # sleep for `UPDATE_DELAY` seconds
    time.sleep(UPDATE_DELAY)
    # get the stats again
    io_2 = psutil.net_io_counters()
    # new - old stats gets us the speed
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
    # print the total download/upload along with current speeds
    print(f"Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
          f"  Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")
    # update the bytes_sent and bytes_recv for next iteration

    DownloadSpeed = get_size(ds)
    
    if DownloadSpeed == "0.00B":
        print("\n\nDownload Speed == 0, Pc shuts down in 10 Minutes!")
        time.sleep(600)
        os.system("shutdown /s /t 1")


    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
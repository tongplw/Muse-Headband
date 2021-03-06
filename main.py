import time
import pandas as pd

from datetime import datetime
from src.muse import MuseMonitor
from src.pylive import live_plot


if __name__ == "__main__":
    
    headset = MuseMonitor("192.168.1.122", 5000)
    time.sleep(5)
    starttime = time.time()
    values = []

    while True:
        time.sleep(0.8)
        attention = headset.attention.value
        meditation = headset.meditation.value
        live_plot(attention, meditation)
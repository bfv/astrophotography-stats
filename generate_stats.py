
from datetime import *
import time
from stat_structures import *

dates = {}

def generate_stats(files):
    
    total_subs = 0
    total_integration = 0

    for file in files:
        dt_str = str(file.date)
        if not dt_str in dates.keys():
            dates[dt_str] = ObservationTarget(file.target, file.date)

        dates[dt_str].subs += 1
        dates[dt_str].integration += file.exposure
        total_subs += 1
        total_integration += file.exposure

    for obs_date in dates:
        obs = dates[obs_date]
        #td = timedelta(seconds=obs.integration)
        hhmm = time.strftime('%Hh %Mm', time.gmtime(obs.integration))
        print(f"target: {obs.target}, date: {obs.date}, subs: {obs.subs}, total integration: {hhmm}")
    
    hhmm = time.strftime('%Hh %Mm', time.gmtime(total_integration))
    print("\ntotals:")
    print(f"  subs: {total_subs}")
    print(f"  integration: {hhmm}")
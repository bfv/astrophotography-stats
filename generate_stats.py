import time
from datetime import timedelta
from stat_structures import *

dates = {}

def convert_to_hhmmss(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%02d:%02d:%02d' % (hour, min, sec)

def generate_stats(files):
    
    total_subs = 0
    total_integration = 0

    for file in files:
        id_str = f"{str(file.date)}-{str(file.target)}" 
        if not id_str in dates.keys():
            dates[id_str] = ObservationTarget(file.target, file.date)

        dates[id_str].subs += 1
        dates[id_str].integration += file.exposure
        total_subs += 1
        total_integration += file.exposure

    dates_sorted = dates  # moet ik nog iets mee
    #dates_sorted = sorted(dates, key=lambda x: a.)
    
    for obs_date in dates_sorted:
        obs = dates[obs_date]
        hhmm = convert_to_hhmmss(obs.integration)
        print(f"target: {obs.target}, date: {obs.date}, subs: {obs.subs}, total integration: {hhmm}")
    
    hhmm = convert_to_hhmmss(total_integration)
    print("\ntotals:")
    print(f"  subs: {total_subs}")
    print(f"  integration: {hhmm}")


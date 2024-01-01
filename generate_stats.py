from stat_structures import ObservationTarget
from fitsfile import FitsFile
from target import targets

dates: dict[str, ObservationTarget] = {}

def convert_to_hhmmss(seconds: int):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%02d:%02d:%02d' % (hour, min, sec)

def generate_stats(files: list[FitsFile]):
    
    total_subs = 0
    total_integration = 0

    for file in files:
        id_str = f"{str(file.date)}-{str(file.target)}" 
        if not id_str in dates.keys():
            dates[id_str] = ObservationTarget(file.target, file.date, file.filter, file.exposure)

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

def sort_dict(d: dict[str, ObservationTarget]) -> dict[str, ObservationTarget]:
    ks = list(d.keys())
    ks.sort()
    sorted = {i: d[i] for i in ks}
    return sorted

def generate_csv(files: list[FitsFile]):

    stats: dict[str, ObservationTarget] = {}
    
    for file in files:
        #print(f"{file.date} {file.filter}")
        ids = f"{file.target}|{str(file.date)}|{file.filter}|{str(file.exposure)}"
        if not ids in stats.keys():
            stats[ids] = ObservationTarget(file.target, file.date, file.filter, file.exposure)
            if file.target == "":
                print(f"------------------------- error: {file.file}")
        
        stats[ids].subs += 1
        stats[ids].integration += file.exposure

    # for stat in stats.keys():
    #     print(stat.key, stat)
    
    ts = sorted(set(targets))
    sorted_stats = sort_dict(stats)
    total_subs, total_integration = 0, 0
    for target in ts:
        subs, integration = 0, 0
        print(target, end='')
        for stat in sorted_stats:
            if stat.startswith(target + '|'):
                print(f";{sorted_stats[stat].date};{sorted_stats[stat].filter};{sorted_stats[stat].subs};{sorted_stats[stat].exposure};{convert_to_hhmmss(sorted_stats[stat].integration)}")
                subs += sorted_stats[stat].subs
                integration += sorted_stats[stat].integration
                total_subs += sorted_stats[stat].subs
                total_integration += sorted_stats[stat].integration
        print(f";;;;;;tot:;{subs};{convert_to_hhmmss(integration)}")
    print()
    print("totals")
    print(f";subs:;{total_subs}")
    print(f"; integration;{convert_to_hhmmss(total_integration)}")


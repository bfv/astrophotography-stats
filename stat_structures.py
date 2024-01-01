
class ObservationTarget:

    def __init__(self, target: str, date: str, filter: str, exposure: int):
        self.target = target
        self.date = date
        self.filter = filter
        self.exposure = exposure
        self.subs = 0
        self.integration = 0
        self.object = object

class MonthData:
    month: int
    subs: int
    integration: int    

    def __init__(self, month: int):
        self.month = month
        self.subs = 0
        self.integration = 0
    
    
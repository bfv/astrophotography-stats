
class ObservationTarget:

    def __init__(self, target: str, date: str, filter: str, exposure: int):
        self.target = target
        self.date = date
        self.filter = filter
        self.exposure = exposure
        self.subs = 0
        self.integration = 0
        self.object = object

class Bicycle:
    def __init__(self, code, station, status="OPERATIVA", repairs=0):
        self.code = code
        self.station = station
        self.status = status
        self.repairs = int(repairs)
        self.saved_pila = None 

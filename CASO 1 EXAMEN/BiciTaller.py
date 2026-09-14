
class BiciTaller:
	

    def __init__(self):
        self.fleet = FleetList()
        self.decommissioned = FleetList()
        self.workshop_queue = Cola()
        self.parts_queue = Cola()
        self.current_bike = None
        self.station_stack = Pila()
        
        
        self.closed_count = 0
        self.suspended_count = 0

    def receive_in_workshop(self, code):
        bike = self.fleet.search(code)
        print(f"RECEIVE {code}")
        if bike is None or bike.status != "REPORTED":
            st = bike.status if bike else "NON-EXISTENT"
            print(f"RECHAZADA (R1): status {st}, bike was not reported")
            return
        bike.status = "IN_TALLER"
        self.workshop_queue.enqueue(bike)

    def start_repair(self):
        print("Start")
        if self.current_bike is not None:
            print("ERROR: Station occupied")
            return
        bike = self.workshop_queue.dequeue()
        if not bike:
            print("No bikes in queue")
            return
        
        self.current_bike = bike
        self.station_stack = Pila()
        
        if bike.saved_pila is not None:
            self.station_stack = bike.saved_pila
            bike.saved_pila = None
            print(f"{bike.code} resumed | Stack restored")

    def disassemble(self, part):
        print(f"DISASSEMBLE {part}")
        if self.current_bike:
            self.station_stack.push(part)

    def assemble(self):
        print("ASSEMBLE")
        if self.station_stack.esta_vacia():
            print("ERROR (R6): Stack empty")
            return None
        return self.station_stack.pop()

    def suspend(self, reason):
        print(f"SUSPEND {reason}")
        if not self.current_bike: return
        
        bike = self.current_bike
        bike.status = "WAIT_REPLACEMENT"
        
        pila_aux = Pila()
        curr = self.station_stack.top
        while curr:
            pila_aux.push(curr.data)
            curr = curr.next
        bike.saved_pila = pila_aux
        
        self.parts_queue.enqueue(bike)
        self.suspended_count += 1
        self.current_bike = None
        print(f"{bike.code} suspended")

    def resume(self, code):
        print(f"RESUME {code}")
        act = self.parts_queue.head
        while act:
            if act.data.code == code:
                bike = act.data
                bike.status = "IN_TALLER"
                self.workshop_queue.enqueue(bike)
                print(f"Bike returned to workshop queue")
                break
            act = act.next

    def close_order(self):
        print("CLOUSE")
        if not self.current_bike: return
        bike = self.current_bike
        
        if not self.station_stack.esta_vacia():
            print(f"rejected (R6): Missing parts on stack")
            return

        bike.repairs += 1
        self.closed_count += 1
        
        if bike.repairs >= 3:
            bike.status = "OFE_low"
            self.decommissioned.insert(bike)
            print(f"{bike.code} DECOMMISSIONED")
        else:
            bike.status = "operational"
        self.current_bike = None


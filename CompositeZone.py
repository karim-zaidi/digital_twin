from Zone import Zone

class CompositeZone(Zone):

    def __init__(self):
        self.zones = []

    def add(self, zone):
        self.zones.append(zone)

    def remove(self, zone):
        self.zones.remove(zone)

    def get_zones(self):
        return self.zones
    
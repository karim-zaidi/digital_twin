from AtomicZone import AtomicZone
from Zone import Zone

class CompositeZone(Zone):

    def __init__(self, zones):
        super().__init__()
        self.zones = []
        self.add(zones)


    # Composition Pattern methods
    def add(self, zone):
        assert isinstance(zone,(Zone,list,tuple))
        if isinstance(zone,(list,tuple)):
            for z in zone:
                self.add(z)
        elif isinstance(zone,Zone):
            self.zones.append(zone)
            zone.is_component = True


    def remove(self, zone):
        self.zones.remove(zone)


    def get_zones(self):
        return self.zones


    # Other methods
    def contains(self, data):
        return any(z.contains(data) for z in self.zones)





# zone1 = AtomicZone()
# zone2 = AtomicZone()
# zone3 = AtomicZone()
# test = CompositeZone(zone1,[zone2,zone3])
# print(test.zones)
    
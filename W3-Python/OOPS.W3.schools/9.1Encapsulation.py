class vwan:
    def __init__(self, hub, gateway):
        self.hub = hub
        self.__gateway = gateway 

    def nva(self):
        return self.__gateway
    
    def firewall(self, gateway):
        if gateway > 0:
            self.__gateway = gateway

        else:
            print("VWAN is an SDWAN solution which is one of the best one")

p2s = vwan("S2Sgateway" , 100)
print(p2s.nva())

#p2s.firewall(626)
#print(p2s.nva())

p2s.firewall(0)
print(p2s.nva())

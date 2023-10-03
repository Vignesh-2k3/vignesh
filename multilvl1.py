class GrandFather:
    def ownHouse(self):
        print("Grandpa House")
class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")
        self.ownHouse()
class Son(Father):
    def ownMobile(self):
        print("Son Have a Mobile phone")
        self.ownBike()
        self.ownHouse()
o = Son()
o.ownMobile()
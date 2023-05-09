from Assets import *

class House(Asset):
    def __init__(self, folioNum, province, description, initialPrice, finalPrice, url, canton, district, direction, house, area):
        super().__init__(folioNum, province, description, initialPrice, finalPrice, url)
        self.canton = canton
        self.district = district
        self.direction = direction
        self.house = house
        self.area = area
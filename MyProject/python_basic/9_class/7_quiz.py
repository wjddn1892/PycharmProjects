# Quiz) 주어진 코들르 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
#
# houses = [house1, house2, house3]
# print("총", len(houses), "대 의 매물이 있습니다.")
# for house in houses:
#     house.show_detail()

# houses = []
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
# print("총", len(houses), "대 의 매물이 있습니다.")
# for house in houses:
#     house.show_detail()
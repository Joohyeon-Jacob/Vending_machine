
import random
import pandas as pd

# 자판기 수익
profit = 0

duration = 7 # 물품 판매 기간(7일)
money = [5000, 1000, 500, 100]
timezone = 17 # 6시 ~ 23시(17시간)
items_info = {'b1': [850], 'b2': [1500], 'b3': [2000], 'c1': [5250], 'c2': [5500]}

for item_info in items_info.values():
    item_info.extend([15, 0])

# items_info --> key: 물품, value: [가격, (남은)물품 개수, 고객 구매 개수]
print(f'items_info_init: {items_info}')

class VendingMachine: # 자판기 class 
    def __init__(self, money, timezone, items_info, beverage_condition='cold'):
        self.money = money # 지불 가능한 현금 종류
        self.timezone = timezone # 판매 가능 시간 e.g. 17시간
        self.items_info = items_info
        self.beverage_condition = beverage_condition

    def calculate(self):
        '''
            자판기 판매 과정 & 판매 수익 return
        '''
        profit = 0
        for _ in range(self.timezone):
            # 시간당 평균 10개 물품 선택한다고 가정
            choice_list = random.choices(list(self.items_info.keys()), k=10)
            # 선택한 물품 가격 정산
            for item in choice_list:
                
                # 고객 제시 금액은 오직 현금(오천원권, 천원권, 오백원 주화, 백원 주화)
                wallet = random.choices(money, k=random.randint(1,4)) # 가지고 있는 현금 조합 random하게 생성
                payment = sum(wallet) # 지불하는 현금 총액

                # input 에 해당하는 물품 개수 남아 있고 물품 가격 <= payment: 1 차감 & profit 업데이트
                if items_info[item][1] > 0 and self.items_info[item][0] <= payment:
                    # print(f'wallet: {wallet}, payment: {payment}, price: {self.price[item]}')
                    # 10원 단위 거스름돈은 돌려주지 않음
                    addition  = self.items_info[item][0] + (payment-self.items_info[item][0]) % 100
                    # print(f'addition: {addition}')
                    profit += addition

                    self.items_info[item][1] -= 1
                    # 고객 선택 항목 기록
                    self.items_info[item][2] += 1
        
        return self.items_info, profit

<<<<<<< Updated upstream
=======
    def display(self):
        """ 음료수 객체 조회, 존재하는 상품의 img show """
        raise NotImplementedError
    


class Drink: # 사용자가 마실때 참고할 기능(?)
    def __init__(self, name, price, property="juice", temperature="cold"):
        raise NotImplementedError
    
    def put_image(self, np_img):
        raise NotImplementedError

    def get_image(self):
        raise NotImplementedError

    def change_temperature(self):
        raise NotImplementedError
        

>>>>>>> Stashed changes
sell_amount = VendingMachine(money, timezone, items_info)
items_info_final, profit = sell_amount.calculate()
print(f'items_info_final: {items_info_final}')
print(f'profit: {profit}')

# items_info_final_df = pd.DataFrame.from_dict(items_info_final)
df = pd.DataFrame(items_info_final)
print(df)

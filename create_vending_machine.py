
import random
import pandas as pd

# 자판기 수익
profit = 0

money = [5000, 1000, 500, 100]
timezone = 17 # 6시 ~ 23시(17시간)
items_info = {'b1': [850], 'b2': [1500], 'b3': [2000], 'c1': [5250], 'c2': [5500]}

item_count = {}
customer_choices = {}

for item_info in items_info.values():
    item_info.extend([15, 0])
    # customer_choices[item] = 0

# items_info --> key: 물품, value: [가격, (남은)물품 개수, 고객 구매 개수]
print(f'items_info_init: {items_info}')

'''
    확장성 있게 vending machine 만들기: Class 통해서 객체화
    e.g. 조건 다양화: 자판기, 현금 지불, 거스름돈, 물품, ... 
'''

class VendingMachine: # 자판기 class 
    def __init__(self, money, timezone, items_info):
        self.money = money # 지불 가능한 현금 종류
        self.timezone = timezone # 판매 가능 시간 e.g. 17시간
        # self.price = price # 물품 가격
        # self.item_count = item_count # 물품 종류
        # self.customer_choices = customer_choices # 고객 선택 기록
        self.items_info = items_info

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

sell_amount = VendingMachine(money, timezone, items_info)
items_info_final, profit = sell_amount.calculate()
print(f'items_info_final: {items_info_final}')
print(f'profit: {profit}')

# items_info_final_df = pd.DataFrame.from_dict(items_info_final)
df = pd.DataFrame(items_info_final)
print(df)

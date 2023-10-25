
import random

# 자판기 수익
profit = 0

money = [5000, 1000, 500, 100]
timezone = 17 # 6시 ~ 23시(17시간)
price = {'b1': 850, 'b2': 1500, 'b3': 2000, 'c1': 5250, 'c2': 5500}
print(f'price: {price}')

item_count = {}
customer_choices = {}

for item in price.keys():
    item_count[item] = 15
    customer_choices[item] = 0

'''
    확장성 있게 vending machine 만들기: Class 통해서 객체화
    e.g. 조건 다양화: 자판기, 현금 지불, 거스름돈, 물품, ... 
'''

class VendingMachine: # 자판기 class 
    def __init__(self, money, timezone, price, item_count, customer_choices):
        self.money = money # 지불 가능한 현금 종류
        self.timezone = timezone # 판매 가능 시간 e.g. 17시간
        self.price = price # 물품 가격
        self.item_count = item_count # 물품 종류
        self.customer_choices = customer_choices # 고객 선택 기록

    def calculate(self):
        '''
            자판기 판매 과정 & 판매 수익 return
        '''
        profit = 0
        for _ in range(self.timezone):
            # 시간당 평균 10개 물품 선택한다고 가정
            choice_list = random.choices(list(self.price.keys()), k=10)
            # 선택한 물품 가격 정산
            for item in choice_list:
                
                # 고객 제시 금액은 오직 현금(오천원권, 천원권, 오백원 주화, 백원 주화)
                wallet = random.choices(money, k=random.randint(1,4)) # 가지고 있는 현금 조합 random하게 생성
                payment = sum(wallet) # 지불하는 현금 총액

                # input 에 해당하는 물품 개수 남아 있고 물품 가격 <= payment: 1 차감 & profit 업데이트
                if item_count[item] > 0 and self.price[item] <= payment:
                    # print(f'wallet: {wallet}, payment: {payment}, price: {self.price[item]}')
                    # 10원 단위 거스름돈은 돌려주지 않음
                    addition = self.price[item] + (payment-self.price[item]) % 100
                    # print(f'addition: {addition}')
                    profit += addition

                    self.item_count[item] -= 1
                    # 고객 선택 항목 기록
                    self.customer_choices[item] += 1
        
        return self.item_count, self.customer_choices, profit

sell_amount = VendingMachine(money, timezone, price, item_count, customer_choices)
remaining_items, customer_choice, profit = sell_amount.calculate()
print(f'remaining_items: {remaining_items}')
print(f'customer_choice: {customer_choice}')
print(f'profit: {profit}')

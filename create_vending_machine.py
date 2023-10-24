
import random

# bevarages = {'b1': 1000, 'b2': 1500, 'b3': 2000}
# cigarettes = {'c1': 5000, 'c2': 5500}
# items = list(bevarages.keys()) + list(cigarettes.keys())
# items_price = {'b1': 1000, 'b2': 1500, 'b3': 2000, 'c1': 5000, 'c2': 5500}
items_price = {'b1': 850, 'b2': 1500, 'b3': 2000, 'c1': 5250, 'c2': 5500}
print('price:',items_price)

item_count = {}
customer_choice_save = {}


# 자판기 채우기(3종류 음료수, 2종류 담배 각각 15개씩)
# for bevarage in bevarages.keys():
#     vendor[bevarage] = 15

# for cigarette in cigarettes.keys():
#     vendor[cigarette] = 15

for item in items_price.keys():
    item_count[item] = 15
    customer_choice_save[item] = 0

print(f'item_init: {item_count}')

# 자판기 수익
profit = 0

# 고객 지불 화폐 단위
money = [5000, 1000, 500, 100]

# 하루에 몇 개의 물품이 팔릴지 정하기 --> 일단 6시 ~ 23시(17시간) 동안 시간당 평균 10개 팔린다고 가정
for _ in range(17):
    # 시간당 팔리는 물품 개수 10개(중복 가능)
    # choice_list = [random.choice(items) for _ in range(10)]
    choice_list = random.choices(list(items_price.keys()), k=10)
    # 선택한 물품 가격 정산
    for item in choice_list:
                
        # 고객 제시 금액은 오직 현금(오천원권, 천원권, 오백원 주화, 백원 주화)
        wallet = random.choices(money, k=random.randint(1,4)) # 가지고 있는 현금 조합 random하게 생성
        payment = sum(wallet) # 지불하는 현금 총액

        # input 에 해당하는 물품 개수 남아 있고 물품 가격 <= payment: 1 차감 & profit 업데이트
        if item_count[item] > 0 and items_price[item] <= payment:
            print(f'wallet: {wallet}, payment: {payment}, price: {items_price[item]}')
            # 10원 단위 거스름돈은 돌려주지 않음
            addition = items_price[item] + (payment-items_price[item]) % 100
            print(f'addition: {addition}')
            profit += addition

            item_count[item] -= 1
            # 고객 선택 항목 기록
            customer_choice_save[item] += 1

print('고객 선택:', customer_choice_save)
print(f'item_final: {item_count}')
print('이익:', profit)

# 커피 가격 300원
# 물품 (커피, 프림, 설탕, 물, 종이컵)
# 물품이 부족할 시 부족하다는 메시지 출력후 종료
# 커피 메뉴에 따라 물품의 소모량은 다름
# 소모후 재료 현황을 업데이트
# 종료 메뉴를 선택하면 남은 돈 반환

# 자판기 재료 현황 : 딕셔너리사용
japangi =  {'환전': 0,
'물의 양' : 500,
'커피량' : 100,
'프림량' : 100,
'설탕량' : 100,
'종이컵량' : 5 }


class VendingMachine:
    def __init__(self, input_dict):
        self.input_money = 0
        self.inventory = input_dict

    def run(self):
        money = int(input('동전을 넣으세요:').strip())
        if money >= 300:
            self.input_money += 300
            if self.inventory['물의 양'] >= 100 and self.inventory['종이컵량'] >= 1:
                while True:
                    print('-'*30)
                    print('1. 블랙커피')
                    print('2. 프림 커피')
                    print('3. 설탕 프림 커피')
                    print('4. 재료 현황')
                    print('5. 종료')
                    print('-'*30)
                    menu = input('원하는 메뉴를 선택하세요.:').strip()
                    
                    if menu == '1':
                        print('-'*30)
                        print('블랙 커피를 선택하셨습니다.')
                        if self.inventory['커피량'] >= 30 and self.inventory['물의 양'] >= 100 and self.inventory['종이컵량'] >= 1:
                            self.inventory['커피량'] -= 30
                            self.inventory['물의 양'] -= 100
                            self.inventory['종이컵량'] -= 1
                            if money > 300:
                                
                                print(f'잔액반환 : {money-300}')
                                money -= 300
                                print('잔돈이 남았음으로 커피를 더 선택 할 수 있습니다.')
                                continue
                        else:
                            print('재료가 부족함으로 종료합니다.')
                            print(f'잔액반환 : {money}')
                            break

                    elif menu == '2':
                        print('-'*30)
                        print('프림 커피를 선택하셨습니다.')
                        if self.inventory['커피량'] >= 15 and self.inventory['프림량'] >= 15 and self.inventory['물의 양'] >= 100 and self.inventory['종이컵량'] >= 1:
                            self.inventory['커피량'] -= 15
                            self.inventory['프림량'] -= 15
                            self.inventory['물의 양'] -= 100
                            self.inventory['종이컵량'] -= 1
                            if money > 300:
                                print(f'잔액반환 : {money-300}')
                                money -= 300
                                print('잔돈이 남았음으로 커피를 더 선택 할 수 있습니다.')
                                continue
                        else:
                            print('재료가 부족함으로 종료합니다.')
                            print(f'잔액반환 : {money}')
                            break

                    elif menu == '3':
                        print('-'*30)
                        print('설탕 프림 커피를 선택하셨습니다.')
                        if self.inventory['커피량'] >= 10 and self.inventory['프림량'] >= 10 and self.inventory['설탕량'] >= 10 and self.inventory['물의 양'] >= 100 and self.inventory['종이컵량'] >= 1:
                            self.inventory['커피량'] -= 10
                            self.inventory['프림량'] -= 10
                            self.inventory['설탕량'] -= 10
                            self.inventory['물의 양'] -= 100
                            self.inventory['종이컵량'] -= 1
                            if money > 300:
                                print(f'잔액반환 : {money-300}')
                                money -= 300
                                print('잔돈이 남았음으로 커피를 더 선택 할 수 있습니다.')
                                continue
                            
                        else:
                            print('재료가 부족함으로 종료합니다.')
                            print(f'잔액반환 : {money}')
                            break
                    
                    elif menu == '4':
                        print('-'*30)
                        print('재료 현황을 출력합니다.')
                        print(f'자판기 커피량 : {self.inventory["커피량"]}g')
                        print(f'자판기 물의 양 : {self.inventory["물의 양"]}ml')
                        print(f'자판기 프림량 : {self.inventory["프림량"]}g')
                        print(f'자판기 설탕량 : {self.inventory["설탕량"]}g')
                        print(f'자판기 컵의 갯수 : {self.inventory["종이컵량"]}개')
                        print('-'*30)
                        continue

                    elif menu == '5':
                        print('프로그램을 종료합니다.')
                        print(f'잔액반환 : {money}')
                        break
                    else:
                        print('1~5의 숫자만 입력하세요!')
            else:
                print('재료가 부족하여 자판기를 사용할 수 없습니다.')
        else:
            print(f'돈 반환 : {money}')
            print('사용 할 수 없는 돈입니다.')

coffe_machine = VendingMachine(japangi) # 변수 = 클래스(변수1)
coffe_machine.run() # 변수.내부def함수()
        
     





# 초기 1회만 동전 투입 메뉴 선택
# 투입된 돈이 300원 이상인 경우에 커피 제공
# 메뉴 출력시 현재 잔액을 화면에 표시
# 메뉴 1. 블랙커피, 2. 프림 커피, 3. 설탕 프림 커피, 4. 재료 현황, 5.종료



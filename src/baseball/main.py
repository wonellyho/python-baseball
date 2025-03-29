#결과출력함수
def print_result(strike, ball):
    
    if(ball!=0 and strike!=0):
        print(f"{ball}볼 {strike}스트라이크")
    elif(ball==0 and strike!=0):
        print(f"{strike}스트라이크")
    elif(ball!=0 and strike==0):
        print(f"{ball}볼")
    else:
        print("낫싱")
    
#게임 시작여부결정함수
def restart_game():
        print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
       
        user_choice=int(input())
        
        if user_choice==2:
        #메인함수 종료 만들기
            return False
        elif user_choice==1:
            return True

def main():


    #1~9까지 서로다른 세자리수 random.sample()로 뽑기
    import random


 
    correct_all_falg=False
    
    print("숫자야구게임을 시작합니다.")
    
    while(1):
        
        com_num_lst=random.sample(range(1,10),3)
        
        while(1):
        # 숫자확인용
            print(com_num_lst)
            
            
            #문자열로 받아오기
            user_num=input("숫자를 입력해주세요 : ")
            
            ball=0
            strike=0
            
            
            # 컴퓨터숫자 사용자 숫자 비교
            for i in range(3):
                for j in range(3):
                     
                    if int(user_num[i])==com_num_lst[j]:
                        if i==j:
                            
                            strike+=1 #스트라이크 처리하면 다른자리랑은 비교x
                            break #볼로 카운트 하지 않는다.
                        else:
                            
                            ball+=1

            print_result(strike,ball)
            
            
            if strike==3:
                print("3개의 숫자를 모두 맞히셨습니다! 게임종료")
                
                if restart_game():
                    #True면 새게임 시작
                    break 
                else:
                    #False면 main함수 종료
                    return 0

                
    
if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()

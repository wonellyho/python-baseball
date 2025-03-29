
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
    



def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    
    
    #1~9까지 서로다른 세자리수 random.sample()로 뽑기
    import random
    
    
    com_num_lst=random.sample(range(1,10),3)
 
    
    
    print("숫자야구게임을 시작합니다.")
    
    while(1):

        print(com_num_lst)
        #문자열로 받아오기
        user_num=input("숫자를 입력해주세요 : ")
        
        ball=0
        strike=0
        
        
        # 컴퓨터숫자 사용자숫자 비교
        for i in range(3):
            for j in range(3):
                
                
                if int(user_num[i])==com_num_lst[j]:
                    if i==j:
                        
                        strike+=1 #스트라이크 처리하면 다른자리랑은 비교x
                        break #볼로 카운트 하지 않는다.
                    else:
                        
                        ball+=1
                
                    #낫싱
                    
                #남은것들과 비교
        print_result(strike,ball)
        #결과출력

        
        
        # if sum(result_lst)==0:
        #     print("낫싱")
        # elif result_lst[0]==0: #스트라이크만 있을때
        #     print(strike+"스트라이크")
        # elif result_lst[1]==0: #볼만 있을때
        #     print(ball+"볼")
        
        #이미 앞에 스트라이크가 되면 볼처리하면안돼돼

              
        
    
    

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()

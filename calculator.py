import random

def selectBehavior(present, opponentNum, minChips, maxChips):
    average = sum(present) / len(present) # 남은 카드의 평균 (정수)
    weight = abs(average-opponentNum) * 10 # 가중치 산출법 
    if minChips == 0:
        length = maxChips - minChips + 1
    else:
        length = maxChips - minChips + 2 # 0, '다이'의 선택지도 빼먹으면 안됨.
    arr = [100/length for _ in range(length)]
    weight += 1/length*10 # 자신의 칩이 적을수록 신중해져야 하므로, 가중치를 높인다.
    if opponentNum == 10: # 상대 카드가 10이면 과감해질 필요가 있음.
        weight += 10
    rweight = weight # 가중치를 임시로 저장해놓는 것임.
    #print(rweight)
    weight /= 10
    while not 100/length - (weight+0.1)*length//2 >= 0:
        weight -= 0.1 # 확률에서 가중치를 빼다보면, 확률이 '-' 이 되는 현상이 있는데 가중치를 줄임으로써 해결함. //예외처리임.
    if (average > opponentNum and (average >= opponentNum * 2 or maxChips >= minChips * 2)) or (opponentNum == 10 and maxChips >= minChips * 4): # 즉, 베팅할만할때만 높은베팅을 시도해봄.
        # 상대방이 평균의 1/2배보다 작으면 상대가 어떻게 베팅하든 계속 높게 베팅. 컴퓨터가 숫자싸움 이길확률 매우 높거든용
        # 상대방이 평균보다 작은 것을 기본 전제로 하면, maxChips 이 minChips의 2배보다 작다면 내꺼가 낮을것이라고 판단하고 사리는 것으로 결정한다.
        # 상대가 10일때는 minChips 를 maxChips 와 비교하여 상대가 끝까지 베팅할 건지 확인함

        # 자신감 뿜뿜, 상대의 숫자가 10 일때는 자신감 뿜뿜인 '척'(블러핑) 하는 것임.
        if length%2 == 0:   # 리스트 길이가 짝수면
            k = 1
            while k <= length//2:
                arr[length//2-k] -= weight * k
                arr[length//2+k-1] += weight * k
                k += 1
        else:               # 리스트 길이가 홀수면
            k = 1
            for i in range(length//2+1, length):
                arr[i] += weight * k
                arr[-i-1] -= weight * k
                k += 1
    elif average < opponentNum:                     # 자신 없음, 내 숫자가 더 작을 위험이 큼
        if length%2 == 0:   # 리스트 길이가 짝수면
            k = 1
            while k <= length//2:
                arr[length//2-k] += weight * k
                arr[length//2+k-1] -= weight * k
                k += 1
        else:               # 리스트 길이가 홀수면
            k = 1
            for i in range(length//2+1, length):
                arr[i] -= weight * k
                arr[-i-1] += weight * k
                k += 1
    else: # 확률이 다 같을 때, 이럴 때는 randint 가 좋음. // 즉, 가중치가 0일때만 이렇게 함.
        situation = random.randint(1,4) # 4번중에 1번만 쪼금 과감하게 하는 것으로.
        if situation < 4:
            if minChips > maxChips//4:
                if minChips > maxChips//2:
                    return random.choice([0, minChips])
                else:
                    return random.choice([0, random.randint(minChips,maxChips//2)])
            else:
                return random.choice([0, random.randint(minChips,maxChips//4)])
        else:
            if minChips > maxChips//2:
                return random.choice([0, minChips])
            else:
                return random.choice([0, random.randint(minChips,maxChips//2)])
    #print(arr) #테스트용, 주석 바람.

    if (average > opponentNum and (average >= opponentNum * 2 or maxChips >= minChips * 2)) or (opponentNum == 10 and maxChips >= minChips * 4):
        behavior = randSelect(arr, rweight, True) #유리하니까 True, 상대가 10 인 경우도 포함되는 것임. 유리한척 블러핑
    else:
        behavior = randSelect(arr, rweight, False) #불리하니까 False
    
    if minChips == 0:
        return behavior
    else:
        if behavior != 0:
            return minChips + behavior - 1
        else:
            return 0

# 상대(컴퓨터)가 사람과 비슷하게 게임할 수 있게 하는 방법
# 1. 가중치에 의해 확률에 가산을 하거나 감산을 한다.
# 2. 이에 그치지 않고 가중치가 높을 수록 과감한 선택을 하게 한다. // 1번만 하면 너무 자주 높게 베팅을 해서..
# 3. 자신의 칩이 적을수록 신중해져야 하므로, 가중치를 높인다.
# 4. 상대 카드가 10이면 과감해질 필요가 있음.

def randSelect(percentArr, weight, advantage): # 몇 번째 원소를 택할까? 랜덤으로 해결한다. 여기서도 가중치가 존재
    if advantage: #유리할때
        if int(weight/2) > 100:
            a = 100
        elif int(weight/2) < 100-len(percentArr)*2:
            a = random.randint(int(weight/2),100-len(percentArr)*2) # 확률 자르기 (최솟값 정하기) 적당히 베팅 너무 성급하게 베팅하면 상대방에게 져주는 느낌임. 최댓값도 유동적임
        elif int(weight/2) < 100-len(percentArr):
            a = random.randint(int(weight/2),100-len(percentArr)) # 확률 자르기 (최솟값 정하기) 적당히 베팅 너무 성급하게 베팅하면 상대방에게 져주는 느낌임. 최댓값도 유동적임
        else:
            a = random.randint(int(weight/2),100) # 확률 자르기 (최솟값 정하기)
        #print(a) #테스트용, 주석 바람.
        b = 0
        for i in percentArr:
            b += i
            #print(b, a)
            if b >= a:
                return percentArr.index(i)
    else: #불리할때
        if not int(100-weight-len(percentArr)) > 0:
            a = 0
        else:
            a = random.randint(0,int(100-weight-len(percentArr))) # 확률 자르기 (최댓값 정하기)
        #print(a) #테스트용, 주석 바람.
        b = 0
        for i in percentArr:
            b += i
            #print(b, a)
            if b >= a:
                return percentArr.index(i)
    return len(percentArr)-1 #예외처리, 솔직히 이게 작동될 확률은 거의 없다고 봐도 됨. (무시가능)

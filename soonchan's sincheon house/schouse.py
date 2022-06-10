n=int(input())
home = []
home.append(list(map(int, input().split())))
building_List = []

def make_m (X_Y_LIST, x_h, y_h) :
    mList = []
    for e in X_Y_LIST :
        mList.append(e[0]-x_h/e[1]-y_h)
    return min(mList), max(mList)

for y in range(1, n+1) : 
    building = []
    building.append(list(map(int, input().split()))) # [x1,y1,x2,y2]
    x1 = building[0]
    y1 = building[1]
    x2 = building[2]
    y2 = building[3]
    Finalbuilding = [[x1, y1], [x2, y1], [x1, y2], [x2, y2]] #x1,y1 x2,y1 x1,y2 x2,y2
    building_List.append(Finalbuilding)

for y in building_List :
    m_max_min_List = []
    a, b = make_m(y, home[0], home[1])
    if -1<b<0 or 0<a<1 :
        pass
    else :
        m_max_min_List.append([a,b]) # min, max

# 1. min 값 구하기
# 2. max값, min 값 저장해둔 후 삭제
# 3. 다시 min값 불러와사 범위 안인지 검사
# 4. 끝까지 돌리다가 범위 벗어나는거 있으면 탈주

min m_max_min_List

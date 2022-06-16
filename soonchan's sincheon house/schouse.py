n=int(input())
home = []
home.append(list(map(int, input().split())))
building_List = []
Yes_or_No = "Yes"
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
    m_min_plus_List = []
    m_min_minus_List = []
    m_max_plus_List = []
    m_max_minus_List = []
    m_mid_max_List = []
    m_mid_min_List = []

    a, b = make_m(y, home[0], home[1])

    if -1<b<0 or 0<a<1 :
        pass
    elif a<0 and b<0 :
        m_min_minus_List.append(a) # min, max
        m_max_minus_List.append(b)

    elif a>0 and b>0 :
        m_min_plus_List.append(a)
        m_max_plus_List.append(b)
    
    else : # 한개는 -, 한개는 +인경우
        m_mid_min_List.append(a)
        m_mid_max_List.append(b)




mid_max_g = max(m_mid_max_List)
mid_min_g = min(m_mid_min_List)

Done = False


max_g = max(m_max_minus_List) 
position = m_max_minus_List.index(max_g)
min_g = m_min_minus_List[position] 
m_max_minus_List.remove(max_g)
m_min_minus_List.remove(min_g)

while not Done :
    max_g = max(m_max_minus_List)
    position = m_max_minus_List.index(max_g)
    if min_g >= max_g :
        pass
    elif min_g <= mid_max_g :
        Done = True
    else :
        Done = True
        Yes_or_No = "No"

    min_g = m_min_minus_List[position]
    m_max_minus_List.remove(max_g)
    m_min_minus_List.remove(min_g)




min_g = min(m_min_plus_List) 
position = m_min_plus_List.index(min_g)
max_g = m_max_plus_List[position] 
m_max_plus_List.remove(max_g)
m_min_plus_List.remove(min_g)

while not Done :
    min_g = min(m_min_plus_List) 
    position = m_min_plus_List.index(min_g)
    if max_g >= min_g :
        pass
    elif max_g <= mid_min_g :
        Done = True
    else :
        Done = True
        Yes_or_No ="No"

    max_g = m_max_plus_List[position] 
    m_max_plus_List.remove(max_g)
    m_min_plus_List.remove(min_g)

print(Yes_or_No)
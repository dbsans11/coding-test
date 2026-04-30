def solution(ing):
    n,st=0,[]
    for i in ing:
        st.append(i)
        if st[-4:]==[1,2,3,1]:
            for _ in range(4): st.pop()
            n+=1
    return n
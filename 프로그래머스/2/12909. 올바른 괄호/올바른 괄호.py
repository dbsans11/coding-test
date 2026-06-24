def solution(s):
    st = []
    for c in s:
        if not st:
            st.append(c)
        else:
            if c=='(':
                st.append(c)
            elif st[-1] != '(':
                return False
            else:
                st.pop()
    return not st
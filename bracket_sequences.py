s=list(input().split())


def right_bracket(s):
    st=[]
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            st.append(s[i])
            continue
        if (s[i]==')' or s[i]=='}' or s[i]==']') and st:
            if (st[-1]+s[i]=='()') or (st[-1]+s[i]=='{}') or (st[-1]+s[i]=='[]'):
                st.pop()
            else:
                return False
        else:
            return False
    if st==[]:
        return True
    else:
        return False

if __name__ == '__main__':
    right_bracket(s)

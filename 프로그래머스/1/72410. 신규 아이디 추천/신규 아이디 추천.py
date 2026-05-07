def solution(new_id):
    new_id=new_id.lower()
    new_id=new_id.translate(str.maketrans('','','~!@#$%^&*()=+[{]}:?,<>/'))
    while '..' in new_id: new_id=new_id.replace('..','.')
    new_id=new_id.strip('.')
    if not new_id: new_id='a'
    if (l:=len(new_id))>=16: new_id=new_id[:15].rstrip('.')
    elif l<=2: new_id+=new_id[-1]*(3-l)
    return new_id
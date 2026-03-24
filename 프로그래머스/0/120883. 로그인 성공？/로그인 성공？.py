def solution(idpw,db):
    db={i:p for i,p in db}
    return 'fail' if not db.get(idpw[0]) else 'login' if db[idpw[0]]==idpw[1] else 'wrong pw'
def solution(id_list, report, k):
    dec, mail, report = {id:0 for id in id_list}, {id:0 for id in id_list}, set(report)
    
    for rep in list(report):
        x, y = rep.split()
        dec[y]+=1
        
    for rep in report:
        x, y = rep.split()
        if dec[y]>=k: mail[x]+=1
    
    return list(mail.values())
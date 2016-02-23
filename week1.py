def function(str,ls,n):
    mes = list(str)
    rs = []
    for i in range(n):
        for count in ls:
           rs.append(mes[count])
        mes = rs
        rs = []
    print ''.join(mes)

function("ABC" ,[2,0,1] ,2)


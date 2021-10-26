def GetLogData(file_name = 'log.txt'):
    file = open(file_name, 'r')
    brasil = chile = mexico = other = 0
    brasilAssinado = chileAssinado = mexicoAssinado = otherAssinado = 0
    
    for line in file.readlines():
        country = line[0:2]
        sign_status = line[-9:-1]
        if country == '55':
            brasil += 1
            if sign_status == 'assinado':
                brasilAssinado+= 1
        elif country == '56':
            chile += 1
            if sign_status == 'assinado':
                chileAssinado+= 1
        elif country == '52':
            mexico += 1
            if sign_status == 'assinado':
                mexicoAssinado+= 1
        else:
            other +=1
            if sign_status == 'assinado':
                otherAssinado+= 1

    toSaveFile = open('logcount.txt', 'w')
    
    toSaveFile.write('Brasil, '+str(brasil)+', '+str(brasilAssinado)+'\nChile, '+str(chile)+', '+str(chileAssinado)+
    '\nMexico, '+str(mexico)+', '+str(mexicoAssinado))
    
    if other>0:
        toSaveFile.write('\nExistem '+str(other)+' registros associados a outros paises, sendo '+str(otherAssinado)+' assinados.')
    
    file.close()
    toSaveFile.close()

GetLogData()

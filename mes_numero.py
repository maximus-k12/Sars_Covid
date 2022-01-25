def mesANumeroInt(mes):
    m = {
        'ENE': "01",
        'FEB': "02",
        'MAR': "03",
        'ABR': "04",
        'MAY': "05",
        'JUN': "06",
        'JUL': "07",
        'AGO': "08",
        'SEP': "09",
        'OCT': "10",
        'NOV': "11",
        'DIC': "12"
        }


    out = str(m[mes])
    return int(out) 
   
def mesANumeroStr(mes):
    m = {
        'ENE': "01",
        'FEB': "02",
        'MAR': "03",
        'ABR': "04",
        'MAY': "05",
        'JUN': "06",
        'JUL': "07",
        'AGO': "08",
        'SEP': "09",
        'OCT': "10",
        'NOV': "11",
        'DIC': "12"
        }


    out = str(m[mes])
    return out    
#print(mesANumero("JUN"))
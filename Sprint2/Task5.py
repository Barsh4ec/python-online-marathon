import re

def max_population(data):
    result = []
    max_pop = 0
    for item in data[1:]:
        if int(re.split(',', item)[2]) > max_pop:
            max_pop = int(re.split(',', item)[2])
            result.clear()
            result.extend(re.split(',', item))
    return (result[1], int(result[2]))



if __name__ == '__main__':
    data = ["id,name,poppulation,is_capital",
            "3024,eu_kyiv,24834,y",
            "3025,eu_volynia,20231,n",
            "3026,eu_galych,23745,n",
            "4892,me_medina,18038,n",
            "4401,af_cairo,18946,y",
            "4700,me_tabriz,13421,n",
            "4899,me_bagdad,22723,y",
            "6600,af_zulu,09720,n"]

    print(max_population(data))